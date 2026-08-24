#!/usr/bin/env python3
"""Cross-file consistency gate (gate 5 of 5).

Checks references BETWEEN data files that validate.py (per-file structure) and
check_public.py (hygiene) do not cover:
  - every storylines tag in vanilla_lore_books.json resolves to a
    vanilla_lore.json storyline id, or is x- prefixed;
  - every contested-question / storyline key_books esm_id exists in
    vanilla_lore_books.json;
  - items.json xref["vanilla-ref"] targets exist in vanilla_ref.json;
  - vanilla_npcs.json trainer/skill and vanilla_lore_books.json skill_book
    names are valid skill names;
  - camp names in camps_events.json camp_base_xp and camp_xp_comparison agree;
  - community_resources entries have name+url (URL liveness only with --online).

Run from repo root: python tools/check_consistency.py [--online]
Exit 1 on any error.
"""
import json, sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
errors, warnings = [], []
def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

SKILLS = {"Block","Armorer","Medium Armor","Heavy Armor","Blunt Weapon","Long Blade","Axe","Spear","Athletics","Enchant","Destruction","Alteration","Illusion","Conjuration","Mysticism","Restoration","Alchemy","Unarmored","Security","Sneak","Acrobatics","Light Armor","Short Blade","Marksman","Mercantile","Speechcraft","Hand-to-hand"}

vl = load("vanilla_lore.json"); vlb = load("vanilla_lore_books.json")
story_ids = {s["id"].split(":",1)[1] for s in vl.get("storylines", [])}
book_esm = {b["esm_id"].lower() for b in vlb["books"]}
for b in vlb["books"]:
    for t in b.get("storylines") or []:
        if t not in story_ids and not t.startswith("x-"):
            errors.append(f"vanilla_lore_books: {b['id']} storyline tag '{t}' unresolved")
    sk = b.get("skill_book")
    if sk and sk not in SKILLS:
        errors.append(f"vanilla_lore_books: {b['id']} skill_book '{sk}' not a skill")
for s in vl.get("storylines", []):
    for kb in s.get("key_books") or []:
        if kb.get("esm_id","").lower() not in book_esm:
            errors.append(f"vanilla_lore: {s['id']} key_book '{kb.get('esm_id')}' not in books file")

vr = load("vanilla_ref.json")
vr_record_ids = {r["id"].lower() for r in vr.get("items", []) if r.get("id")}
it = load("items.json")
for r in it.get("items", []):
    tgt = (r.get("xref") or {}).get("vanilla-ref")
    if tgt and tgt.lower() not in vr_record_ids:
        errors.append(f"items: {r['id']} xref vanilla-ref '{tgt}' not a vanilla_ref record id")

vn = load("vanilla_npcs.json")
for n in vn.get("npcs", []):
    for sk in (n.get("trainer_top3") or []):
        if sk not in SKILLS:
            errors.append(f"vanilla_npcs: {n['esm_id']} trainer skill '{sk}' not a skill")

ce = load("camps_events.json")
cx = {c["camp"].replace(" (solo)","") for c in (ce.get("camp_xp_comparison") or {}).get("group_xp_per_minute", [])}
cb = {c["camp"] for c in (ce.get("camp_base_xp") or {}).get("camps", [])}
for c in cb - cx: warnings.append(f"camps: base-xp camp '{c}' absent from xp comparison")
for c in cx - cb: warnings.append(f"camps: comparison camp '{c}' absent from base-xp table")

for fname in ("mechanics.json","alchemy.json"):
    d = load(fname)
    for cr in (d.get("_meta") or {}).get("community_resources", []) or []:
        if not cr.get("name") or not cr.get("url"):
            errors.append(f"{fname}: community_resources entry missing name/url")
if "--online" in sys.argv:
    import urllib.request
    for fname in ("mechanics.json","alchemy.json"):
        for cr in (load(fname).get("_meta") or {}).get("community_resources", []) or []:
            try:
                urllib.request.urlopen(urllib.request.Request(cr["url"], method="HEAD", headers={"User-Agent":"np-codex-linter"}), timeout=10)
            except Exception as e:
                warnings.append(f"{fname}: community resource '{cr['name']}' URL check failed: {e}")

for w in warnings: print("WARN:", w)
if errors:
    print(f"FAIL — {len(errors)} error(s):")
    for e in errors: print("  -", e)
    sys.exit(1)
print(f"check_consistency: OK ({len(warnings)} warnings)")
