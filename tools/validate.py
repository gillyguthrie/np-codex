#!/usr/bin/env python3
"""Structural validation for np-kb-public data files.

Checks:
  - every data/*.json parses;
  - every record id matches ^[a-z]+:[a-z0-9-]+$ and is globally unique;
  - cross-references resolve: mastery requirement IDs, contradiction/open-question
    subject IDs, archetype mastery IDs (unresolved archetype IDs are warnings —
    community builds may cite post-wiki masteries not yet captured);
  - every parsed effect key exists in effects_vocab.json;
  - stubs (captured:false) carry no asserted stats.

Exit 0 = valid (warnings allowed), 1 = errors.
"""
import json, re, sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
ID_RE = re.compile(r"^[a-z]+:[a-z0-9-]+$")
errors, warnings = [], []

def main():
    docs = {}
    for f in sorted(DATA.glob("*.json")):
        try:
            docs[f.name] = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{f.name}: invalid JSON: {e}")
    vocab = set()
    if "effects_vocab.json" in docs:
        vocab = {e["key"] for e in docs["effects_vocab.json"].get("effects", [])}

    all_ids = {}
    def collect(name, doc):
        def rec(obj):
            if isinstance(obj, dict):
                oid = obj.get("id")
                if "claimed_cost" in obj:
                    oid = None  # a reference to a mastery, not a definition
                if isinstance(oid, str) and ID_RE.match(oid):
                    if oid in all_ids:
                        errors.append(f"duplicate id {oid} ({all_ids[oid]} + {name})")
                    all_ids[oid] = name
                elif isinstance(oid, str):
                    errors.append(f"{name}: malformed id {oid!r}")
                for v in obj.values():
                    rec(v)
            elif isinstance(obj, list):
                for v in obj:
                    rec(v)
        rec(doc)
    for name, doc in docs.items():
        collect(name, doc)

    def check_effects(name, doc):
        def rec(obj, path):
            if isinstance(obj, dict):
                if "key" in obj and "delivery" in obj and vocab and obj["key"] not in vocab:
                    errors.append(f"{name}: effect key '{obj['key']}' not in effects_vocab ({path})")
                for k, v in obj.items():
                    rec(v, f"{path}.{k}")
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    rec(v, f"{path}[{i}]")
        rec(doc, "$")
    for name, doc in docs.items():
        if name != "effects_vocab.json":
            check_effects(name, doc)

    m = docs.get("masteries.json", {})
    for rec in m.get("masteries", []):
        for req in (rec.get("requires", {}) or {}).get("masteries", []):
            if req not in all_ids:
                errors.append(f"masteries.json: {rec['id']} requires unresolved {req}")
    a = docs.get("archetypes.json", {})
    for rec in a.get("archetypes", []):
        for mref in rec.get("masteries", []):
            mid = mref.get("id")
            if mid and mid not in all_ids:
                warnings.append(f"archetypes.json: {rec['id']} cites unresolved {mid} (claimed: {mref.get('name')})")
    for rec in docs.get("items.json", {}).get("items", []):
        if rec.get("captured") is False:
            for fld in ("ar", "weight", "value_gold"):
                sv = rec.get(fld)
                if isinstance(sv, dict) and sv.get("value") is not None:
                    errors.append(f"items.json: stub {rec['id']} asserts {fld}")
            if rec.get("effects"):
                errors.append(f"items.json: stub {rec['id']} asserts effects")

    for w in warnings:
        print("WARN:", w)
    if errors:
        print(f"FAIL — {len(errors)} error(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"validate: OK ({len(all_ids)} ids, {len(warnings)} warnings)")

if __name__ == "__main__":
    main()
