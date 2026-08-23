# Changelog

## 2026-08-23 — v0.3.1 vanilla world data (locations, NPCs, spells)
- **New `data/vanilla_locations.json`** (~2,079 items): where vanilla items are actually found — world placements by cell, containers, NPC carriers, RESTOCKING sellers, and leveled-list membership — parsed from the ESMs' CELL/CONT/NPC_/CREA/LEVI records. Answers "where can I find a Daedric Helm?" with real cells. Developer test cells excluded. Vanilla baseline; per-record np_override door left open.
- **New `data/vanilla_npcs.json`** (633 service NPCs): merchants with barter gold, trainers (top-3 skills where stored; autocalc = null per populated-or-null), spellmakers/enchanters, with cell + faction.
- **New `data/vanilla_spells.json`**: all 1,065 vanilla spells (typed, with effect blocks) + 141 magic effects with school and base cost.
- SKILL.md: rule 8 extended (vanilla item locations answered in-codex from the baseline), file map +3, and item-stat lookups now show the tooltip screenshot by default when the record has an image. `np-codex.skill` repackaged.
- Quests and NPC dialogue deliberately NOT ingested — UESP remains the referral for walkthroughs.
- Creature souls deliberately NOT ingested (system believed reworked on NP) — + `q:np-soul-rework` with the working hypothesis (charge value vanilla, merchant gold value nerfed; unverified).

## 2026-08-23 — v0.3.0 vanilla lore layer
- **New `data/vanilla_lore_books.json`**: all 449 distinct in-game books, notes, scrolls, and letters from the Morrowind/Tribunal/Bloodmoon ESMs, each SUMMARIZED IN ORIGINAL WORDS (never reproduced) with type, skill-book mapping, topics, characters, factions/places, and storyline tags. IP convention in `_meta`: the KB holds summaries only; verse is described, never quoted; full-text requests are declined with a pointer to the in-game book.
- **New `data/vanilla_lore.json`**: 15 synthesized storyline arcs (Nerevarine prophecy, Tribunal & Dagoth Ur, Dwemer mystery, Great Houses, ...) plus 6 **contested questions** (What happened at Red Mountain? Are the Tribunal divine? Where did the Dwemer go? ...) with each competing tradition attributed to its sources. Binding `contested_is_canon` convention: Morrowind's core lore contradictions are authored content — answered by presenting the traditions flatly, never resolved.
- **SKILL.md rule 7 amended**: vanilla lore is now answered IN-CODEX from these files, never from the internet; UESP referral narrows to quests/NPCs/anything the vanilla files don't cover. File map +2 entries; `np-codex.skill` repackaged.
- Vanilla-only scope: NP-server lore remains in lore.json for future NP-specific additions.

## 2026-08-23 — v0.2.3 werewolf-alchemy facts + movement (provisional) + per-mob XP
- mechanics.json: `fact:ww-potion-buffing` (human-form potion buffs persist into beast form; Alchemy 100 + Cowl of the Druid advised) and `fact:ww-gear-no-transfer` (gear stats don't carry into WW form except the Endowment robe/skirt) — from the public werewolf build guide (player-builds, 2025-09-28). Fixes the persona eval's weakest answer.
- mechanics.json: `formula:movement-speed` (walk/run/sneak/swim/fly with engine-GMST constants) — PROVISIONAL, new `s-sheet-prov` source; the workbook tab labels itself "possibly accurate" and the record says so.
- camps_events.json: `camp_base_xp` — base XP per kill for 30 mob variants across all 13 camps (pre-bonus values; compose with fact:xp-kill-bonus-stacking and fact:party-xp-split).

## 2026-08-23 — v0.2.3 community calculators workbook ingest
- Ingested the community "Spreadsheet Calculators" workbook (maintainer-provided export; Google Sheets blocks automated fetch). New `s-sheet` source in mechanics/enchanting/camps_events.
- **enchanting.json**: `ench:charge-cost-formula` — charges/cast = ROUNDUP(EV x (1.1 - EnchantSkill/100)), min 1 — which converges exactly with the long-standing `ench:one-charge-110` fact; new `ev_caps` table (9 item classes, Daedric Tower Shield 225 down to Exquisite robe/belt/shoes 40).
- **mechanics.json**: 6 new formulas — absorb/reflect multiplicative stacking (explicit form), armor damage mitigation (max(0.25, swing/(swing+AR)) — 75% reduction floor), melee hit chance, evasion, lockpick/probe success, elemental-shield damage (provisional) — plus 2 facts: kill-XP bonus stacking (best-of luck/potion/Cheer + clothing + HH) and measured party XP-split multipliers. formula:hp gains independent corroboration of the HF-adds-to-ratio structure.
- **camps_events.json**: `camp_xp_comparison` — 13-camp XP/min ranking (Tomb > Dreugh > Twilights > ... > Mudcrabs) with the sheet's buff configuration stated.
- **_meta community_resources** added to mechanics.json and alchemy.json: point users to the community wiki, the calculators site, and the recipe finder as living resources.

## 2026-08-23 — v0.2.2 spell-cast-chance formula (community tool)
- mechanics.json: + `formula:spell-cast-100-cost` — max spell cost castable at 100%: floor(2*skill + will/5 + luck/10 + specBonus - fatigueTerm), fatigueTerm 80 (full fatigue) to ~133.33 (zero); specBonus per spec cast-chance perk (Sorcerer +20, Channeler +40, mages +0, Combat -25, Stealth -50). Read verbatim from the source code of the community spell-chance calculator on the NP-Server-Items site; new `s-ctool` source (community-dataset, player-reported tier — not dev-stated).

## 2026-08-23 — v0.2.2 skill rule 9: per-file conventions are binding
- SKILL.md gains rule 9: every data file's `_meta.conventions` block is binding for that file (read before computing); SKILL.md itself changes only for cross-cutting rules or new files, with per-file reading rules living in `_meta`. Codifies the scaling policy — topic expansions (like today's alchemy work) ship without touching the skill. `np-codex.skill` repackaged.

## 2026-08-23 — v0.2.2 alchemy NP-delta capture (Discord sweep)
- **mechanics.json: 8 new alchemy facts** from a full public-archive sweep (server-general, in-game chat, player-builds, player-trades; ~1,130 alchemy-related messages reviewed): active-potion limit values (5 at Alchemy 100, +1 from Cowl of the Druid → 6), 5 potions per combine fully equipped, server-side potion magnitude/duration caps with the resist/elemental-shield/fatigue exceptions and persisting "pre-nerf" batches (era-tagged), potion strength input priority (Alchemy > INT > Luck, ~1 pt lost per skipped max source) and the current-era max-potion meta, ingredient-eating gives first effect only, Vampire Dust's Vampirism is cosmetic, mass-brew anti-cheat/lag caution (~100 per combine practice), and a publicly-accounted ~950 CM alchemist budget. New sources `s-sgen`, `s-igchat` (public channels, player-reported).
- **alchemy.json: first np_ingredients record** — `ingr:elemental-flame-dust` stub (2026 Infernal Flame Atronach Camp drop, in-game chat 2026-08-09; effects unknown); np_ingredients note now names the known-but-uncaptured fireshield-fish drop ingredient. Counts gain `np_custom_stubs`.
- **items.json**: Cowl of the Druid's +1-active-potion hidden effect upgraded suspected → **corroborated** (three independent public reports, 2025-07 to 2026-03).
- **contradictions.json**: + `c:secret-master-apparatus-impact` — era-2022 "plain Master apparatus suffices at max perks" vs 2026 meta "full Secret Master set"; unresolved, era change likely.
- Post-release persona eval (13 simulated player questions) caught two defects, fixed same day: fact:potion-active-limit-values overstated a second +1-potion item (only the Cowl of the Druid is attested — reworded); duplicate vanilla ESM records under one display name (8 names, e.g. Daedra's Heart x2) could over-count computed answers — alchemy.json now carries a count-by-name convention and `vanilla_distinct_names: 118`.
- **open_questions**: `q:np-custom-ingredients` and `q:np-process-deltas` updated (partially answered); + `q:potion-limit-curve`, `q:potion-count-composition`, `q:apparatus-tier-impact`.

## 2026-08-23 — v0.2.1 alchemy + vanilla process baselines
- **New `data/alchemy.json`**: 126 vanilla ingredients parsed from the game ESMs (effects in game order — reveal order matters), with an `np_ingredients` section for server-added ingredients (confirmed to exist per Aug 2026 chat — names not yet captured → `q:np-custom-ingredients`). Checked: "Sticky Cinnamon Taffy" is Jiubsmas throwing ammo, not an ingredient.
- **New `data/vanilla_processes.json`**: how vanilla alchemy, enchanting, and armor repair actually work — GMST constants parsed from the ESMs (fWortChanceValue 15, iSoulAmountForConstantEffect 400, fRepairAmountMult 3, etc.), the game's own enchanting help text verbatim, and engine-documented formula structure (new `engine-docs` origin). Purpose: the fixed baseline to diff NP's modified processes against → `q:np-process-deltas`. NP enchanting answers stay in enchanting.json.
- SKILL.md file map updated for both; `np-codex.skill` repackaged.

## 2026-08-23 — v0.2.1 answer style + README overhaul
- SKILL.md answering style rewritten from a style audit (8 persona questions): answer-first and confident; zero process narration (no file names, internal fields, or "per the KB's rule"); caveats collapsed to one trailing line and only when load-bearing; resolved contradictions stated as plain fact; "not in the KB" answers capped at two sentences + the Discord pointer; no unsolicited offers. `np-codex.skill` repackaged.
- README rebuilt as the **Nerevarine Prophecies Codex** front page: TOC, what's-in-this-repo summary, and step-by-step "How to use Claude with this Codex" / "How to use ChatGPT with this Codex" sections.

## 2026-08-23 — v0.2.1 effects backfill + audit gate
- **146 tooltip effect lines backfilled** into parsed `effects[]` across 111 items — the full sweep behind the builder thread's 64-line Fortify Skill list, extended to every effect type: skill fortifies, attribute drains (Chronium Pendant's full 8-attribute drain set), weaknesses (stored as negative resist magnitudes), restores, detects, and more. Each carries its verbatim raw_text and a backfill note.
- **Structured params**: every `fortify-skill` effect now carries a `skill` field and every `drain-attr` an `attr` field (81 params added to existing records) — tools no longer parse raw_text to learn which skill/attribute. New vocab keys: drain-hp, drain-mag, drain-fat.
- **Delivery corrections** (the Whitefang class): Glacier Splitter's Resist Frost is a 10-sec on-strike buff, not constant; Book of Lore's four effects are 65-sec timed, not constant. Bulbor's Cooking Knife speed 135%/range 6ft recovered from misfiled tooltip lines.
- **New gate: `tools/audit_effects.py`** — fails if any tooltip line lacks a parsed effect or any timed raw line is curated as constant. This class of drift is now machine-caught; run it with validate + check_public before every commit.
- open_questions: + `q:weapon-stat-capture-gaps` (7 weapons without damage, ~117 without speed — OCR/in-game backlog).

## 2026-08-23 — v0.2.1 vanilla reference
- **New `data/vanilla_ref.json`**: 1,584 vanilla equipment records (armor/weapons/clothing incl. jewelry, 847 with enchantments) parsed directly from the game's Morrowind/Tribunal/Bloodmoon ESM files. New `game-esm` origin in the provenance enum. NP vanilla-named items now carry `xref["vanilla-ref"]` (50 matched).
- **ESM extraction corrected two memory-sourced KB claims**: (1) the piece-AR note's "vanilla Daedric Tower Shield 45" — the ESM says base 80; (2) q:vanilla-modified-tracking's entire "NP buffed artifact damage" list (Sunder/Goldbrand/Hopesfire/Eltonbrand/Skull Crusher) and the Mantle of Woe claim — all identical to vanilla in the ESM. The question is now partially resolved with the real, ESM-verified NP changes: Wraithguard + Marara's Ring Reflect 20->10, Marara's lost Fortify Acrobatics, Nordic Silver Battleaxe + Stormfang retuned, and armor AR systematically reduced (~half of vanilla, some helms further).
- SKILL.md rule 7 updated: vanilla item stats now answerable from vanilla_ref.json (with the AR-convention warning); vanilla lore/quests still go to UESP. `np-codex.skill` repackaged.

## 2026-08-23 — v0.2.1 persona-test round 2
- camps_events.json: the winter event now carries its community name — **"Jiubsmas"** — as an alias, with the ornament-quest / event-limited-drops note; items whose location reads "Jiubsmas" (e.g. Whitefang) now cross-reference it via drop_notes.
- open_questions.json: + `q:player-theft-rules` (rules are silent on pickpocketing/looting other players), `q:elemental-camp-level-ranges` (no level guidance for atronach/event camps), `q:race-base-stats` (races.json has abilities only — no base attribute/skill tables).
- mechanics.json: `formula:sheet-ar` note tells tool authors how to locate flat Armor Bonus masteries (no enumerated registry yet).
- SKILL.md: era preference clarified as data-currency, not advice (fit recommendations to the player's level/goals); speculative-fragments handling added to rule 3 (label speculation, never stitch it into an established-sounding answer). `np-codex.skill` repackaged.

## 2026-08-23 — v0.2.1 skill-test fixes
- birthsigns.json: Atronach Wombburn `magmult` effect now carries the **adopted** 1.2× value (dev-doc 1.25× kept verbatim in raw_text with an editorial resolution note) — resolves the two-pass answer where single-file readers computed with the superseded figure.
- contradictions.json: `c:vampire-ancient-bloodline-rmag` subject corrected from `sign:atronach` to `mastery:ancient-bloodline` (copy-paste error).
- SKILL.md rule 4 rewritten: resolved contradictions are reported as their adopted value, only unresolved ones as contested. `np-codex.skill` repackaged to match.

## 2026-08-23 — v0.2.1 persona-test round (3 simulated users, 10 questions)
- items.json: **Whitefang** effects corrected — Fortify Attack 50 was curated as constant but the posted tooltip is a timed 30-sec on-strike effect (full Light/Paralyze/Attack enchant set now parsed). `light` added to effects_vocab.
- archetypes.json: new machine-readable `cost_semantics` field on every record (`per-mastery` = summable, `cumulative` = running total, read the final entry) — prevents the 15,275-point mis-sum on the Ascetic builds; two mis-spelled mastery references fixed (`bulging-muscles-4`, `talos-blessing-5`).
- masteries.json: stubs added for **Champion Master Class** and **Disenchant** (cited by build posts, absent from the wiki capture) → new open question `q:missing-masteries-archetype-cited`.
- camps_events.json: both fire camps now carry `status` + disambiguation notes (long-standing Nchuleftingth camp vs the 2026 Infernal Flame event camp).
- open_questions.json: + `q:weapon-speed-attack-rate` (no speed%→swing-rate formula, blocks exact DPS comparisons).
- SKILL.md policy: the codex is **NP-only** — vanilla lore/stats questions are referred to the UESP Morrowind wiki; unknown values and missing item locations are referred to **#server-general on the NP Discord**; item-location questions answer from the `location`/`drop_notes` fields; file map now carries sizes + fetch-economy guidance; archetype `cost_semantics` and camp-era rules added. `np-codex.skill` repackaged.

## 2026-08-22 — v0.1.0 initial migration
- Repo scaffolded: governance, schemas, tools, data layout.
- (entries appended per migration batch below)

## 2026-08-22 — v0.1.0 content
- mechanics.json:  constants, formulas, facts migrated with provenance; AR skill-100 convention declared.
- birthsigns.json + races.json: 0.8 dev tables verbatim (13 signs, 10 races).
- masteries.json: 885 wiki-captured masteries + 3 known-gap stubs (Rend, Cleave, Combo Focus 4).
- items.json: 634 catalog items + 58 hand-captured (Sunder, Keening, Wraithguard, Eltonbrand, Skull Crusher, Ebony Mail, artifacts); 1 self-enchant excluded by policy.
- camps_events.json (23 camps, 11 events, 42 facts), lore.json (36 entries), archetypes.json (26 depersonalized builds), server_rules.json, enchanting.json.
- contradictions.json (8) + open_questions.json (25) seeded from the research ledger.
- Tooltip images deferred to a follow-up release (image audit pending).

## 2026-08-23 — v0.2.0 upstream reconciliation (NP-Server-Items by Skooma Breath, with permission)
- Cross-checked all 605 upstream records against the KB: 586 matched (xref recorded on each), 13 new items added (gear only; ammo/consumables skipped by policy).
- 35 constant effects restored from our own posted tooltip text (upstream corroborated); 8 pixel-verbatim corrections adjudicated from tooltip screenshots (Wind Golem set Str->Agi + End 30, White Wind Shock/Frost weaknesses, Scorched Right Pauldron Agi 50).
- 137 hidden-effect reports and 1 spec requirement ingested (community-reported, marked suspected).
- 585 tooltip images added under images/items/ (audited; named by item id).
- New origin "community-dataset"; tools/ingest_upstream.py + upstream.json added for repeatable update checks.

## 2026-08-23 — origin_game classification
- Every item classified vanilla / np-custom against the actual Morrowind + Tribunal + Bloodmoon ESM rosters (2,749 display names): 52 vanilla-named, 653 server-custom.
- New open question q:vanilla-modified-tracking (NP demonstrably buffs several vanilla artifacts — damage +5..15, Mantle of Woe 0.5x->5.0x INT); systematic flagging deferred.
- schema/item.schema.json + docs updated.

## 2026-08-23 — community skill renamed
- The in-repo assistant skill is now named np-codex (was np-kb-public).

## 2026-08-23 — remote-first skill
- np-codex skill rewritten remote-first: users install only np-codex.skill; it fetches data/*.json live from this repo (local clone optional). np-codex.skill added to the repo root as the download; README install note.

## 2026-08-23 — provenance review
- Charlatan's Glove and Glove of Divination briefly removed as suspected self-enchants, then restored after owner review confirmed they are genuine server items (public tooltip posts, Nov 2023). Visage of Mzund and Finely Tailored Robes verified as genuine (owner-held No Trade items, in-game tooltip captures on file).
- README: added instructions for using the skill outside Claude (paste SKILL.md into ChatGPT).

## 2026-08-23 — owner provenance review, round 2
- Finely Tailored Robes removed: owner-confirmed player self-enchant (blocklisted in migration tooling). Items: 704.
- Visage of Mzund verified with a fresh tooltip capture (image added): No Trade heavy helm, CE Fortify Fatigue 60; reported as a Skyrim Loot Cache rare drop (unconfirmed).
