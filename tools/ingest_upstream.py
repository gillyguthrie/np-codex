#!/usr/bin/env python3
"""Check the upstream NP-Server-Items community dataset for updates.

Compares the CURRENT upstream data against tools/upstream_snapshot.json — the
fingerprint of what this KB last ingested — so only genuine upstream changes are
reported (new items, removed items, edited records). Never writes to data/;
applying changes is always a reviewed, deliberate step.

Usage:
  python tools/ingest_upstream.py                          # clone + diff
  python tools/ingest_upstream.py --offline PATH_TO_CLONE  # diff a local clone
  python tools/ingest_upstream.py --resnapshot PATH        # after applying changes:
                                                           # refresh snapshot + commit pin
"""
import json, re, hashlib, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "upstream.json"
SNAP = Path(__file__).parent / "upstream_snapshot.json"

def fingerprint(rec):
    payload = json.dumps({
        "e": sorted(rec.get("Effects") or []),
        "s": {k.strip(): str(v).strip() for k, v in (rec.get("Stats") or {}).items()},
        "h": (rec.get("Hidden Effect(s)") or "").strip(),
        "req": [(rec.get("Lvl Req.") or "").strip(), (rec.get("Spec. Req.") or "").strip()],
        "loc": (rec.get("Location/Boss/Event") or "").strip(),
    }, sort_keys=True)
    return hashlib.sha1(payload.encode()).hexdigest()[:16]

def load_upstream(clone, cfg):
    data = json.loads((clone / cfg["data_file"]).read_text(encoding="utf-8"))
    return {re.sub(r"\s+", " ", r["Item Name"]).strip(): r for r in data}

def main():
    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode in ("--offline", "--resnapshot") and len(sys.argv) > 2:
        clone, head = Path(sys.argv[2]), "(local)"
    else:
        tmp = tempfile.mkdtemp(prefix="npkb_upstream_")
        subprocess.run(["git", "clone", "--depth", "1", cfg["repo"], tmp], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clone = Path(tmp)
        head = subprocess.run(["git", "-C", tmp, "rev-parse", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
        if head == cfg.get("last_ingested_commit") and mode != "--resnapshot":
            print(f"up to date: upstream HEAD {head[:10]} already ingested.")
            return
    now = load_upstream(clone, cfg)
    if mode == "--resnapshot":
        SNAP.write_text(json.dumps({n: fingerprint(r) for n, r in now.items()},
                                   indent=0, sort_keys=True), encoding="utf-8")
        if head != "(local)":
            cfg["last_ingested_commit"] = head
            CFG.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
        print(f"snapshot refreshed ({len(now)} records)" + ("" if head == "(local)" else f"; pinned {head[:10]}"))
        return
    snap = json.loads(SNAP.read_text(encoding="utf-8")) if SNAP.exists() else {}
    added = sorted(set(now) - set(snap))
    removed = sorted(set(snap) - set(now))
    edited = sorted(n for n in set(now) & set(snap) if fingerprint(now[n]) != snap[n])
    print(f"upstream HEAD: {head} | records: {len(now)}")
    print(f"new: {len(added)} | removed: {len(removed)} | edited: {len(edited)}")
    if added or removed or edited:
        out = [f"# Upstream diff — HEAD {head}", ""]
        for title, names in (("New items", added), ("Removed items", removed), ("Edited records", edited)):
            if names:
                out.append(f"## {title}")
                out += [f"- {n}" for n in names]
                out.append("")
        (Path(__file__).parent / "upstream_diff.md").write_text("\n".join(out), encoding="utf-8")
        print("wrote tools/upstream_diff.md — review, apply deliberately, then run --resnapshot")
    else:
        print("no content changes.")

if __name__ == "__main__":
    main()
