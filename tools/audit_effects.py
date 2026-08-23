#!/usr/bin/env python3
"""Effects audit gate: verify every effects_raw_posted tooltip line on every item
is represented in the parsed effects[] (and flag delivery mismatches).

This is the gate that catches the "Whitefang class" of bug (a timed effect curated
as constant) and the "Fortify Skill class" (a tooltip line silently dropped from
effects[]). Run from the repo root:  python tools/audit_effects.py
Exit code 1 if any uncovered line or delivery mismatch is found.
"""
import json, re, sys

d = json.load(open('data/items.json'))
v = json.load(open('data/effects_vocab.json'))
name2key = {e['name'].lower(): e['key'] for e in v['effects']}

SKILLS = ["blunt weapon","long blade","medium armor","heavy armor","light armor","short blade","hand-to-hand","hand to hand","block","armorer","axe","spear","athletics","enchant","destruction","alteration","illusion","conjuration","mysticism","restoration","alchemy","unarmored","security","sneak","acrobatics","marksman","mercantile","speechcraft","blunt"]
ATTRS = ["strength","intelligence","willpower","agility","speed","endurance","personality","luck"]
ALIAS = {"resist common disease":"disease","resist blight disease":"blight","resist disease":"disease",
 "restore health":"restore-hp","restore magicka":"restore-mag","restore fatigue":"restore-fat",
 "drain health":"drain-hp","drain magicka":"drain-mag","drain fatigue":"drain-fat",
 "detect animal":"detect","detect enchantment":"detect","detect key":"detect",
 "resist magicka":"rmag","resist fire":"fire","resist frost":"frost","resist shock":"shock","resist poison":"poison"}
WEAK = {"weakness to fire":"fire","weakness to frost":"frost","weakness to shock":"shock","weakness to magicka":"rmag","weakness to poison":"poison","weakness to common disease":"disease","weakness to blight disease":"blight"}
SKIP = {'constant effect','','none','cast when used','cast on strike','cast when strikes'}

def parse_line(line):
    l = line.strip().lower()
    if l in SKIP: return None
    onstrike = bool(re.search(r'on (touch|target)\b', l))
    l2 = re.sub(r'\s+on (self|touch|target|strike)\b', '', l)
    m = re.search(r'for (\d+) secs?', l2); dur = int(m.group(1)) if m else None
    l2 = re.sub(r'\s*for \d+ secs?', '', l2)
    base = re.sub(r'\s*\d+(?:\.\d+)?\s*(?:pts?|%|ft)?\s*$', '', l2).strip()
    base = base.replace('fortify attribute ','fortify ').replace('drain attribute ','drain ').replace('damage attribute ','damage ').replace('fortify skill ','fortify ')
    if base.startswith('fortify '):
        rest = base[8:]
        for sk in SKILLS:
            if rest == sk or rest == sk.replace(' ', ''):
                return ('fortify-skill', dur, onstrike, sk)
    if base.startswith('drain '):
        rest = base[6:]
        for a in ATTRS:
            if rest == a: return ('drain-attr', dur, onstrike, a)
    for table in (WEAK, ALIAS):
        if base in table and table[base]: return (table[base], dur, onstrike, None)
    if base in name2key: return (name2key[base], dur, onstrike, None)
    best = None
    for nm, k in name2key.items():
        if base.startswith(nm) and (best is None or len(nm) > len(best[0])): best = (nm, k)
    if best: return (best[1], dur, onstrike, None)
    return ('?', dur, onstrike, None)

uncovered, deliv_mismatch, unparsed = [], [], []
for r in d['items']:
    effs = r.get('effects') or []
    ekeys = {}
    for e in effs: ekeys.setdefault(e['key'], []).append(e)
    for line in (r.get('effects_raw_posted') or []):
        p = parse_line(line)
        if not p: continue
        k, dur, onstrike, param = p
        if k == '?': unparsed.append((r['name'], line)); continue
        matches = ekeys.get(k, [])
        if param:
            matches = [e for e in matches if param in (str(e.get('raw_text','')) + str(e.get('skill','')) + str(e.get('attr',''))).lower()]
        if not matches:
            uncovered.append((r['name'], line)); continue
        if dur and all(e.get('delivery') == 'constant' for e in matches):
            deliv_mismatch.append((r['name'], line))

fail = False
if uncovered:
    fail = True
    print(f"UNCOVERED tooltip lines (raw text with no matching parsed effect): {len(uncovered)}")
    for n, l in uncovered[:20]: print(f"  - {n}: {l}")
if deliv_mismatch:
    fail = True
    print(f"DELIVERY mismatches (timed raw line, constant parsed effect): {len(deliv_mismatch)}")
    for n, l in deliv_mismatch[:20]: print(f"  - {n}: {l}")
if unparsed:
    print(f"note: {len(unparsed)} raw lines not understood by this audit (informational):")
    for n, l in unparsed[:10]: print(f"  - {n}: {l}")
print("audit_effects:", "FAIL" if fail else "clean")
sys.exit(1 if fail else 0)
