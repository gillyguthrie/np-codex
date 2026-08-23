# Changelog

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
