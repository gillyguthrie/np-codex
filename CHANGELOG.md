# Changelog

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
