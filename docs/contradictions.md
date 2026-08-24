<!-- GENERATED from data/contradictions.json by tools/generate_docs.py — do not hand-edit. -->

# Known Contradictions

Both values are kept, dated. Never state an unresolved entry flatly.


## Atronach Fortify Maximum Magicka multiplier — **RESOLVED**

- 1.25x INT (2022-05-10 — 0.8 dev doc, verbatim)
- 1.2x INT (2026-08-21 — in-game tooltip, screenshot-verbatim ('Wombburn 1.2x INT'))

**Resolution:** The in-game tooltip (1.2) is adopted as truth for computation; the doc value may be outdated or the shipped value differs from the doc. mechanics const:magicka-mult-atronach = 1.2.

## Maximum attainable Speed — **UNRESOLVED**

- 350 with Speed perks (2021-02-01)
- 175 default cap at L60 without CM investment (2024-09-11 — later and more specific; may reflect a system change)

## NPC training sessions per day — **RESOLVED**

- 5 per earth day (2022-05-10 — 0.8 notable-changes doc)
- 10 per day (+5 from players) (undated — new-player-thread claim)

**Resolution:** Dev doc wins: 5 per earth day.

## House repossession rule — **UNRESOLVED**

- removed if not entered for 4 weeks (timer updates only on entering) (2019-08-13)
- repossessed if under 10 hours playtime per month (2020-04-14)

*The dev-stated 4-week entry rule should be treated as authoritative pending further data.*

## Do enchanted items recharge without soul gems? — **UNRESOLVED**

- No passive recharge since 0.8; filled soul gems required (2022-05-10)
- Items recharge naturally based on the wearer's Enchant skill (effectively infinite charges at 110) (2020-10-29 — multiple corroborations 2019-2022, some predating 0.8)

*Possibly skill-gated recharge vs passive recharge being different things, or a pre/post-0.8 change. One in-game test settles it.*

## HP spec ratios (3.6/2.8/2.2) vs dev Lua multipliers (1.14/1.033/1.077) — **RESOLVED**

- Lua spec multipliers 1.14/1.033/1.077 (2021-02-26)
- Effective L60 ratios 3.6/2.8/2.2 (2026-08-21)

**Resolution:** Both describe the same system: the Lua multipliers are the spec factor inside it; the effective ratios fold in the remaining layers. Validated exact (Stealth) and within 1 HP (Magic). Combat 3.6 still unvalidated; Magic 2.2-vs-2.19 rounding open.

## Anvil max armor AR gain — **UNRESOLVED**

- +42 AR flat (estimated) (2026-02)
- x1.54 piece AR (one measured fresh-vs-maxed pair at matched skill/condition) (2026-08-22)

*The measured pair (+135 tooltip) does not match the flat estimate; mechanism (flat/base/multiplier) unresolved.*

## Ancient Bloodline magicka-resistance penalty — **RESOLVED**

- -100 magicka resistance (undated — one wiki passage)
- -20 Fire and -20 Magicka Resistance (cumulative -30/-30 with Daywalker) (undated — wiki catalog row, corroborated by an independent 2025 community summary)

**Resolution:** Catalog row adopted (-20/-20). A 2023 dev musing with different numbers was pre-ship planning, superseded by shipped values.

## Does Secret Master apparatus affect max potion potency? — **UNRESOLVED**

- Max-value potions achievable with a plain Master apparatus set given maxed alchemy perks and skill (Breton) (2022-12-16)
- Current max-potion meta includes the full Secret Master apparatus set (2026-01-17)

*Era difference likely explains the conflict: public 2025-04-03 reports of 'pre-nerf' brewing show the potion system changed at least once between these dates. Treat the 2026 position as current-era guidance; resolution needs a same-ingredient tier comparison (q:apparatus-tier-impact).*

## Active-potion limit at Alchemy 100 — **UNRESOLVED**

- 6 at Alchemy 100+ (curve 3/4/5/6 at <50/50-74/75-99/100+) (2019-07-05 — dev announcement introducing the system)
- 5 at Alchemy 100, with the Cowl of the Druid raising it to 6 (2026-08-18 — consistent multi-source current-era player reports)

*Era gap of seven years — a retune between 2019 and 2025 is likely but no announcement for it was found in the updates digest. Resolution: count max active potions in-game at Alchemy 100 without the Cowl (TODO in-game test list).*
