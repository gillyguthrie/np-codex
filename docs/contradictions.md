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

## Does magicka scale with INT above 175 when the INT cap is raised by Fortification Max? — **RESOLVED**

- Flat cap: maxMag uses min(INT, 175) regardless of any raised cap (2026-08-21 — One L60 reading matched floor(min(181,175) x 3.7) = 647 exactly — but came from a session with known-unstable pool readings (duplicate ability applications observed the same day).)
- Cap-relative: magicka scales with INT up to the effective cap (175 base + Intelligence Fortification Max); 175 is just the un-raised base (2026-08-24 — maintainer-stated game mechanic)

**Resolution:** Cap-relative adopted (maintainer ruling 2026-08-24): formula:magicka uses min(INT, INT_cap). The 2026-08-21 flat-cap reading is attributed to that session's unstable pool readings.

## Ancient Shrouded glove AR: 46, 46.5, or a 49-reading normalized? — **OPEN**

- 46 (as-posted wiki tooltip; capture skill unknown) (2026-08-25 — Both wiki tooltip images (left and right glove) read Armor Rating 46.)
- 46.5 (curated skill-100 value carried by the codex and, until v1.21, one builder record pair) (2026-08-22 — Origin of the .5 not reconstructed; possibly a normalization of a non-100-skill capture.)
- 49 (maintainer's own in-game tooltip capture, 2026-08-19; capture Light Armor skill unrecorded) (2026-08-25 — Normalizes to ~46-46.5 if the capturing character's Light Armor was ~106-107; the capturing character's Light Armor value at capture settles this.)

*Builder v1.21 carries 46 (dedup kept the wiki-image pair) pending resolution; one Light Armor reading from the capturing character normalizes the 49 and closes this.*

## What is the magicka pool's base multiplier? A clean-character reading contradicts the validated formula. — **RESOLVED**

- Additive carriers on a x1 base: pool = min(INT, cap) x (1 + racial + sign). Validated exact 2026-08-21 (647 = floor(175 x 3.7) on an Altmer/Atronach at capped INT). (2026-08-21 — The validating character is a vampire main; the maintainer now suspects vamp/WW characters may carry hidden/bugged passives (cf. the separate known single-character magicka/fatigue anomaly already in the KB), so this validation may be contaminated - or only valid at capped INT.)
- Pool much larger than (1+r+s) x INT: a CLEAN L60 Breton/Atronach (naked, zero masteries spent, no vamp/WW, INT 100, WIL 115, active-effects list showing exactly 'Magicka Bonus 0.5x INT' + 'Wombburn 1.2x INT') reads max magicka 469 where the formula predicts 270. (2026-08-25 — Best-fitting hypothesis: a level-scaled base multiplier (~3.0 at L60) giving (3.0+0.5+1.2) x 100 = 470 vs 469 observed (off by one - floor?); but that model gives 997 for the 2026-08-21 reading's character, so the two measurements cannot both fit one simple model. A flat +199 level term fits the clean reading but not the capped one either. The dev-stated Magicka spec factor 1.5 (fact:spec-hp-magicka-factors) fits neither (405).)
- Level-scaled pool: maxMag = floor(INT x (spec_magicka_factor + carriers + ~0.025 x level)) - the dev-stated spec factors (Combat 0.9 / Stealth 1.15 / Magic 1.5) ARE live in the pool, base is NOT 1 x INT. (2026-08-25 — Second clean reading, L1 Combat Redguard/Steed naked (no carriers): 27 = floor(0.9 x 30 + ~0.025x1x30) EXACT - 1 x INT would give 30. Under this model the L60 clean reading predicts 470 vs 469 observed (one short - the same off-by-one as the L60 HP reading, suggesting per-level floor accumulation). The 2026-08-21 validation (647 = 3.7 x 175) still conflicts: under this model that character (Magic spec, Altmer/Atronach, L60) predicts 5.7 x min(INT,cap) = 997 at INT>=175 - but that session had known-unstable readings, and 647/5.7 = 113.5 hints the character's real INT at capture may have been ~113, not 175+. A naked re-read of that character settles it.)

**Resolution:** Level-scaled model ADOPTED (maintainer-measured 2026-08-25, three clean readings): maxMag = floor(min(INT, cap) x (spec_magicka_factor + 0.025 x level + carriers)). Confirmed exact at L1 (27) and L60 (712 = floor(125 x 5.7)); the 469-vs-470.0 reading is an integer-boundary display quirk, not a model failure. The 2026-08-21 position (pool = min(INT,cap) x (1+r+s), '647 validated') is invalidated: no integer INT reproduces 647 under any model, and that session had documented duplicate-ability instability. The same character re-read naked 2026-08-25 fits the new model exactly, which also clears the vampire-contamination suspicion for that character.

*Decisive next tests: (1) Fortify INT item delta on the clean L60 - delta per INT point = the true marginal multiplier (~4.69-4.7 under the level model); (2) one naked MID-level alt reading - pins the ~0.025/level term and the off-by-one behavior; (3) naked re-read of the 2026-08-21 validation character (vamp main) - tests both the contamination suspicion and the INT-113 hypothesis.*
