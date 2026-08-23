---
name: np-codex
description: "Public knowledge base for the Nerevarine Prophecies (NP) TES3MP Morrowind server. ALWAYS use this skill for any question about NP: items, weapons, masteries (CM/mastery points), birthsigns, racials, formulas (HP/Magicka/Fatigue/Armor Rating), camps, bosses, events, enchanting, the Infusion Anvil, server rules, or lore — and for building any tool on NP data. Answers MUST come from the KB's data files (fetched live from the np-codex GitHub repo), never from model memory: NP rewrites vanilla Morrowind values, so remembered vanilla/UESP numbers are wrong here."
---

# NP Codex — community knowledge base skill

This skill is self-contained: you do NOT need a local copy of the knowledge base. Answers come from the live data files in the public repo, so every user always queries the current version.

**Data root:** `https://raw.githubusercontent.com/gillyguthrie/np-codex/main/`

## How to answer any NP question

1. Pick the data file for the topic (map below).
2. Fetch it from the data root (e.g. `.../main/data/mechanics.json`). Always fetch from the repo — it is the single source of truth, and fetching live means every answer reflects the current version. Do not answer from a local copy of the data unless the user explicitly directs you to one.
3. Read or compute the answer from that JSON — with code, for anything multi-number.
4. If web access is unavailable in the session, do NOT answer from memory: say so, and ask the user to paste the relevant data file or grab it from https://github.com/gillyguthrie/np-codex.

## The rules (binding — full text in GOVERNANCE.md at the repo root)

1. **Never state a load-bearing number from memory.** Every magnitude, cost, %, formula constant, or stat must come from the fetched `data/*.json` in the moment, or be computed by code over it. This applies to conversation, not just documents.
2. **NP is not vanilla Morrowind.** If a value "feels known" from vanilla or UESP, that is the signal to look it up — never to answer from training data. (Canonical trap: the Atronach birthsign has Spell Absorption 15 on NP, not vanilla's 50.)
3. **If the KB doesn't know, say so and stop.** A `null` value with a status, or a missing record, means "not in the KB" — report that, check `data/open_questions.json` for a matching known gap, and do NOT fill the hole from any outside knowledge. There is no fallback.
4. **Contested values are reported as contested.** Check `data/contradictions.json`; present both positions with dates, never one of them flatly.
5. **Respect confidence tiers**: dev-stated > measured > player-reported > provisional > contested. Provisional values (e.g. Melding %/rank, anvil AR multiplier) must be flagged as provisional when used.
6. **Dates and eras matter.** Patch-sensitive values (anvil, camps, meta) carry dates/era tags; prefer current-era values and say when a figure is old.

## Which file answers what (all under `data/`)

- `mechanics.json` — formulas, constants, established facts (HP/Magicka/Fatigue/AR formulas, caps, tick length, proc rates). **Tool authors: import constants from here — never hardcode.**
- `items.json` — all server items, weapons included (~700 records). AR values use the skill-100 tooltip convention (see `formula:ar-capture-normalization` in mechanics.json); `captured:false` records are known-to-exist stubs; `origin_game` marks vanilla-named vs server-created items.
- `masteries.json` — the mastery tree (~890 records). `raw_text` is the authoritative effect wording; multi-rank families stack additively (buying rank N implies ranks 1..N summed).
- `birthsigns.json`, `races.json` — the 0.8 dev rework tables, verbatim; `vanilla_note` fields are context only, never valid NP values.
- `camps_events.json` — camps, bosses, holiday events. `enchanting.json` — self-enchant ceilings + Infusion Anvil (era-tagged). `server_rules.json` — rules verbatim. `lore.json` — server lore. `archetypes.json` — community build archetypes (player-reported, costs as claimed).
- `effects_vocab.json` — the effect vocabulary; every parsed effect's `key` and `delivery` class resolve here. `raw_text` on any record beats its parsed form when they disagree.
- `contradictions.json`, `open_questions.json` — known conflicts and known gaps. Check before calling anything settled.
- `docs/` (repo) — generated human-readable pages of the same data, for browsing. `images/` — tooltip screenshots, illustrative only: never re-derive a stat from an image; if a screenshot appears to contradict the data, report it as a suspected correction rather than trusting either side silently.

## Answering style

- Simple lookups: one sentence — the value plus its confidence/date when relevant.
- Multi-number questions: numbered list, one fact per line, arithmetic shown explicitly ("5+10+15 = 30"), computed by code over the data when more than trivial.
- Loadouts/gear: one slot per line with the relevant stats. Comparisons: side-by-side with all key stats inline.

## Contributing

Corrections and additions go through the repo: https://github.com/gillyguthrie/np-codex (issues or pull requests, per GOVERNANCE.md). A contribution needs a source — public channel + date, a tooltip screenshot, or an in-game measurement. The KB names no individuals and never references private channels.
