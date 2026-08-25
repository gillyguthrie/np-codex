#!/usr/bin/env python3
"""Generate docs/*.md from data/*.json. Docs are VIEWS — never hand-edit them."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA, DOCS = ROOT / "data", ROOT / "docs"
HDR = "<!-- GENERATED from data/{src} by tools/generate_docs.py — do not hand-edit. -->\n\n"

def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def w(name, src, text):
    (DOCS / name).write_text(HDR.format(src=src) + text, encoding="utf-8")
    print("wrote", name)

def svs(v):
    if not isinstance(v, dict):
        return str(v)
    if v.get("value") is None:
        return f"— ({v.get('status', 'unknown')})"
    s = str(v["value"])
    if v.get("status") in ("provisional", "contested"):
        s += f" ({v['status']})"
    return s

def fx_summary(effects):
    parts = []
    for e in effects or []:
        mag = e.get("magnitude")
        tag = "" if e.get("delivery") == "constant" else f" [{e.get('delivery')}]"
        if e.get("key") == "unknown":
            parts.append(f"{e.get('raw_text','?')}{tag}")
        else:
            parts.append(f"{e['key']} {mag if mag is not None else ''}{tag}".strip())
    return "; ".join(parts)

def mechanics():
    d = load("mechanics.json")
    out = ["# NP Mechanics — constants, formulas, facts\n",
           f"> {d['_meta']['banner']}\n"]
    out.append("\n## Constants\n\n| id | name | value | unit | note |\n|---|---|---|---|---|")
    for c in d["constants"]:
        val = c.get("value")
        if val is None:
            val = c.get("range", f"— ({c.get('status','unknown')})")
        out.append(f"| `{c['id']}` | {c['name']} | **{val}** | {c.get('unit') or ''} | {c.get('note','') or ''} |")
    out.append("\n## Formulas\n")
    for f in d["formulas"]:
        out.append(f"### {f['name']}  \n`{f['expr']}`  \n{f.get('note','')}\n")
    out.append("\n## Established facts\n")
    for f in d["facts"]:
        flag = " **[provisional]**" if f.get("status") == "provisional" else (" **[contested]**" if f.get("status") == "contested" else "")
        out.append(f"- **{f['id'].split(':',1)[1]}**{flag}: {f['statement']}")
    w("mechanics.md", "mechanics.json", "\n".join(out) + "\n")

def items():
    d = load("items.json")
    out = ["# NP Server Items\n",
           f"{d['_meta']['description']}\n",
           f"\nTotal: {len(d['items'])} items.\n",
           "\n| name | cat | slot/side | AR@100 | wt | effects | hidden |\n|---|---|---|---|---|---|---|"]
    for it in sorted(d["items"], key=lambda x: x["name"].lower()):
        eff = fx_summary(it.get("effects"))
        hid = it.get("hidden_effects", {})
        hidtxt = "" if hid.get("status") in (None, "none") else (hid.get("raw_text") or hid.get("status") or "")
        side = f"{it.get('slot') or it.get('category','')}{' /' + it['side'] if it.get('side') else ''}"
        wtv = it.get("weight", {}).get("value")
        kindtxt = it['item_kind'] + (' · vanilla' if it.get('origin_game') == 'vanilla' else '')
        out.append(f"| {it['name']} | {kindtxt} | {side} | {svs(it.get('ar'))} | {wtv if wtv is not None else ''} | {eff} | {hidtxt} |")
    stubs = [i for i in d["items"] if not i.get("captured")]
    if stubs:
        out.append("\n## Known but not yet captured\n")
        for s in stubs:
            out.append(f"- {s['name']}")
    w("items.md", "items.json", "\n".join(out) + "\n")

def masteries():
    d = load("masteries.json")
    out = ["# NP Masteries\n", f"{d['_meta']['description']}\n"]
    bysec = {}
    for m in d["masteries"]:
        bysec.setdefault(m["section"], []).append(m)
    for sec, ms in bysec.items():
        out.append(f"\n## {sec}\n\n| mastery | cost | requirements | effect |\n|---|---|---|---|")
        for m in ms:
            req = []
            r = m.get("requires", {})
            if r.get("level"): req.append(f"L{r['level']}")
            for a, v in (r.get("attributes") or {}).items(): req.append(f"{a} {v}")
            for mid in r.get("masteries", []): req.append(mid.split(":", 1)[1])
            if r.get("other"): req.append(r["other"])
            cap = "" if m.get("captured") else " **(not yet captured)**"
            out.append(f"| {m['name']}{cap} | {svs(m.get('cost'))} | {', '.join(req)} | {m.get('raw_text','')} |")
    w("masteries.md", "masteries.json", "\n".join(out) + "\n")

def signs_races():
    for fn, key, title in (("birthsigns.json", "birthsigns", "NP Birthsigns (0.8 rework)"),
                           ("races.json", "races", "NP Racials (0.8 rework)")):
        d = load(fn)
        out = [f"# {title}\n", f"{d['_meta']['description']}\n"]
        for r in d[key]:
            out.append(f"\n## {r['name']}\n")
            for a in r["abilities"]:
                out.append(f"- **{a['name']}** ({a['kind']}): {a['raw_text']}")
            if r.get("vanilla_note"):
                out.append(f"\n  *Vanilla (NOT valid on NP):* {r['vanilla_note']}")
        w(fn.replace(".json", ".md"), fn, "\n".join(out) + "\n")

def camps():
    d = load("camps_events.json")
    out = ["# NP Camps, Bosses & Events\n"]
    for c in d.get("camps", []):
        era = f" *(era {c['era']})*" if c.get("era") else ""
        out.append(f"\n## {c['name']}{era}\n")
        if c.get("location"): out.append(f"Location: {c['location']}  ")
        if c.get("mobs"): out.append(f"Mobs: {', '.join(c['mobs'])}  ")
        for b in c.get("bosses", []):
            drops = f" — drops: {', '.join(b['notable_drops'])}" if b.get("notable_drops") else ""
            out.append(f"- Boss: **{b['name']}**{drops}{(' — ' + b['notes']) if b.get('notes') else ''}")
        for m in c.get("mechanics", []):
            out.append(f"- {m['statement']}")
    out.append("\n# Events\n")
    for e in d.get("events", []):
        out.append(f"\n## {e['name']}\n")
        if e.get("schedule"): out.append(f"Schedule: {e['schedule']}  ")
        for m in e.get("mechanics", []): out.append(f"- {m['statement']}")
        if e.get("drops"): out.append(f"- Drops: {', '.join(e['drops'])}")
    out.append("\n# Camp & event facts\n")
    for f in d.get("facts", []):
        out.append(f"- **{f['topic']}**: {f['statement']}")
    w("camps_events.md", "camps_events.json", "\n".join(out) + "\n")

def lore():
    d = load("lore.json")
    out = ["# NP Server Lore\n"]
    for e in d["entries"]:
        out.append(f"\n## {e['topic']}\n\n{e['summary']}\n")
        for f in e.get("facts", []):
            out.append(f"- {f['statement']}")
    w("lore.md", "lore.json", "\n".join(out) + "\n")

def archetypes():
    d = load("archetypes.json")
    out = ["# Community Build Archetypes\n", f"{d['_meta']['description']}\n", f"\n> {d['_meta'].get('caveat','')}\n"]
    for a in d["archetypes"]:
        out.append(f"\n## {a['name']}\n")
        line = [x for x in [a.get("spec"), a.get("archetype"), a.get("race"), a.get("birthsign"), a.get("vampire_or_werewolf")] if x]
        if line: out.append(" · ".join(line) + "\n")
        if a.get("masteries"):
            ms = ", ".join(f"{m['name']}{(' (' + str(m['claimed_cost']) + ')') if m.get('claimed_cost') else ''}" for m in a["masteries"])
            out.append(f"**Masteries (as claimed):** {ms}\n")
        for k, lab in (("gear_notes", "Gear"), ("key_numbers", "Key numbers"), ("strategy_notes", "Strategy"), ("reception_notes", "Reception"), ("era_notes", "Era notes")):
            if a.get(k): out.append(f"**{lab}:** {a[k]}\n")
    w("archetypes.md", "archetypes.json", "\n".join(out) + "\n")

def rules():
    d = load("server_rules.json")
    out = ["# NP Server Rules (verbatim)\n", f"{d['_meta']['description']}\n"]
    for rs in d["rulesets"]:
        out.append(f"\n## {rs['name']} (revised {rs.get('revised','')})\n")
        if rs.get("text"): out.append(rs["text"] + "\n")
        for r in rs.get("rules", []):
            out.append(f"{r['n']}. {r['text']}")
    w("server_rules.md", "server_rules.json", "\n".join(out) + "\n")

def enchanting():
    d = load("enchanting.json")
    out = ["# NP Enchanting & Infusion Anvil\n", f"{d['_meta']['description']}\n"]
    base = d["self_enchant_baseline"]
    out.append(f"\n## Self-enchant baseline (observed maxima)\n\n{base['description']}\n")
    out.append("| slot | fortify | restore HP | levitate/jump | other |\n|---|---|---|---|---|")
    for s in base["slots"]:
        other = []
        for k in ("resist_elemental", "resist_paralysis"):
            if s.get(k) is not None: other.append(f"{k.replace('_',' ')} {s[k]}")
        if s.get("notes"): other.append(s["notes"])
        out.append(f"| {s['slot']} | {s.get('fortify') if s.get('fortify') is not None else '?'} | {s.get('restore_health') if s.get('restore_health') is not None else ''} | {s.get('levitate_jump','') or ''} | {'; '.join(other)} |")
    rr = base["cost_ratios"]
    out.append(f"\n**EV cost ratios** (fortify=1.0x, ~±20%): " + ", ".join(f"{k} {v}x" for k, v in rr["ratios"].items()))
    out.append("\n## Facts\n")
    for f in d["facts"]:
        flag = " **[provisional]**" if f.get("status") == "provisional" else ""
        out.append(f"- {f['statement']}{flag}")
    a = d["anvil"]
    out.append(f"\n## Infusion Anvil ({a['era']})\n\n{a['description']}\n")
    for cv in a["current_values"]:
        out.append(f"- **{cv['item_class']}**: {cv['max_6of6_critical']}{(' — ' + cv['note']) if cv.get('note') else ''}")
    for f in a["facts"]:
        out.append(f"- {f['statement']}")
    w("enchanting.md", "enchanting.json", "\n".join(out) + "\n")

def services():
    d = load("services.json")
    out = ["# NP Player Services\n", f"{d['_meta']['description']}\n"]
    for svc in d["services"]:
        out.append(f"\n## {svc['name']}\n")
        if svc.get("vendor_npc"):
            out.append(f"**Service NPC:** {svc['vendor_npc']} — {svc['vendor_location'] if isinstance(svc.get('vendor_location'), str) else ''}\n")
        elif isinstance(svc.get("vendor_location"), dict):
            out.append(f"**Location:** — ({svc['vendor_location'].get('status','unknown')}){(' ' + svc['vendor_location']['note']) if svc['vendor_location'].get('note') else ''}\n")
        for m in svc.get("mechanics", []):
            flag = f" *[{m['status']}]*" if m.get("status") else ""
            out.append(f"- {m['statement']}{flag}")
        if svc.get("catalog"):
            out.append("\n| Home | Price |\n|---|---|")
            for c in svc["catalog"]:
                out.append(f"| {c['name']} | {c['price_gold']:,} gold ({c['price_as_displayed']}) |")
        for cat in svc.get("exchange", []):
            out.append(f"\n### {cat['category']}\n")
            if cat.get("note"): out.append(cat["note"] + "\n")
            out.append("| Item | Cost (Login Points) |\n|---|---|")
            for i in cat["items"]:
                out.append(f"| {i['name']} | {i['cost_points']} |")
        if svc.get("notes"):
            out.append(f"\n*{svc['notes']}*")
    w("services.md", "services.json", "\n".join(out) + "\n")

def contradictions_oq():
    d = load("contradictions.json")
    out = ["# Known Contradictions\n", "Both values are kept, dated. Never state an unresolved entry flatly.\n"]
    for c in d["contradictions"]:
        out.append(f"\n## {c['topic']} — **{c['status'].upper()}**\n")
        for p in c["positions"]:
            out.append(f"- {p['value']} ({p.get('date','undated')}{(' — ' + p['note']) if p.get('note') else ''})")
        if c.get("resolution"): out.append(f"\n**Resolution:** {c['resolution']}")
        if c.get("note"): out.append(f"\n*{c['note']}*")
    w("contradictions.md", "contradictions.json", "\n".join(out) + "\n")
    d = load("open_questions.json")
    out = ["# Open Questions\n", "Known unknowns and provisional values. Check here before treating an absence as an oversight.\n"]
    for q in d["questions"]:
        out.append(f"- **{q['topic']}** [{q['status']}]{(': ' + q['detail']) if q.get('detail') else ''}")
    w("open_questions.md", "open_questions.json", "\n".join(out) + "\n")

if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    mechanics(); items(); masteries(); signs_races(); camps(); lore(); archetypes(); rules(); enchanting(); services(); contradictions_oq()
    print("docs generated.")
