# Governance — how this knowledge base stays trustworthy

This repo is a community knowledge base for the **Nerevarine Prophecies (NP)** TES3MP server. Its purpose is to be an accurate, machine-readable source of information about the server — items, masteries, birthsigns, races, mechanics, camps, events, and rules — that anyone can read or build tools on.

## The prime directive: NP is not vanilla Morrowind

NP deliberately rewrites vanilla values. Birthsigns and racials were fully reworked in 0.8; item bases differ from vanilla/UESP; core formulas are server-custom. **If a value "feels known" from vanilla Morrowind, that is the signal to look it up here — never to assume it.** Examples of traps: the Atronach birthsign has Spell Absorption **15** on NP (vanilla 50); the Daedric Tower Shield has base AR **40** (vanilla 45).

## Data model rules

1. **`data/*.json` is the sole authority.** Everything in `docs/` is generated from it by `tools/generate_docs.py` and must never be hand-edited. If data and docs disagree, the docs are stale — regenerate them.
2. **Populated-or-null.** Every load-bearing value is either populated with a source reference, or explicitly `null` with a status (`"unknown"`). Blank-filling from vanilla, UESP, memory, or guesswork is prohibited. A gap is a visible TODO, not a silently invented number.
3. **Stable IDs.** Every entity has an immutable slug `id` (e.g. `item:keening`). IDs never change once published; display names can. Cross-references are by ID only. Known variant spellings live in `aliases`.
4. **Verbatim numbers.** Magnitudes, percentages, costs, and formulas are copied exactly from their source. Original tooltip/effect text is preserved in `raw_text` fields; parsed representations never replace it.
5. **Every fact carries provenance**: an `origin` (dev-doc / wiki / discord-public / in-game-tooltip / in-game-measured / player-reported / community-dataset / game-esm / engine-docs), a date, and a confidence tier. Sources are cited by **role and public channel only — this KB names no individuals.** Private channels are never cited or referenced.
6. **Confidence tiers** (highest to lowest): `dev-stated` (server dev's own statements/docs) → `measured` (verified by in-game measurement) → `player-reported` (community statements, plausible but unverified) → `provisional` (a working number from limited evidence) → `contested` (conflicting sources on file). Tools should present `provisional`/`contested` values with their status, never flatly.
7. **Conflicts are kept, dated.** When sources disagree, both values live in `data/contradictions.json` with their dates. Later info supersedes but never deletes earlier info. Patch-sensitive values carry an `era` tag; the anvil system alone was reworked twice, so era matters.
8. **Facts age.** Anything older than ~a year on a patch-sensitive topic should be treated as possibly stale unless re-verified.

## Rules for assistants and tools built on this KB

- **Never state a load-bearing number from memory.** Read it from `data/*.json` or compute it from that data in the moment.
- **If a value is null/unknown here, say "not in the KB" and stop.** Do not fill the gap from vanilla Morrowind, UESP, or training data — on this server those numbers are wrong more often than right.
- Report `contested` values as contested, with both candidates and dates.
- Check `data/open_questions.json` before treating an absence as an oversight — it may be a known gap.

## Contributing

Corrections and additions are welcome. A contribution must include its source (public channel + date, screenshot of an in-game tooltip, or an in-game measurement description). Run `python tools/validate.py` before submitting — it enforces the schema, ID resolution, and the populated-or-null rule. `python tools/check_public.py` enforces repo hygiene (no private-channel references, no person-identifying fields).

## Scope

In scope: server mechanics, items, masteries, birthsigns/races, camps/events, enchanting, rules, lore. Out of scope: any information about individual players or staff, moderation matters, and personal inventories. This KB is about the game, not the people.
