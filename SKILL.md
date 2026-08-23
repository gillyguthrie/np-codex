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
3. **If the KB doesn't know, say so — then point at the community.** A `null` value with a status, or a missing record, means "not in the KB" — report that, check `data/open_questions.json` for a matching known gap, and do NOT fill the hole from any outside knowledge. Instead, direct the user to ask in the **#server-general channel of the Nerevarine Prophecies Discord** — the community is the living source for anything the KB hasn't captured yet. When the KB has only scattered speculative fragments on a topic (records tagged as speculation/provisional), say plainly that the KB has no settled answer, present the fragments clearly labeled as speculation, and point to Discord — don't stitch fragments into something that reads as established.
4. **Check `data/contradictions.json` before calling anything settled — and read its `status`.** A record with `status: "resolved"` is settled: report the adopted value from its `resolution` field as the answer (the competing positions are an optional footnote, not a live dispute). Only an unresolved record is contested: present both positions with dates, never one of them flatly.
5. **Respect confidence tiers**: dev-stated > measured > player-reported > provisional > contested. Provisional values (e.g. Melding %/rank, anvil AR multiplier) must be flagged as provisional when used.
6. **Dates and eras matter.** Patch-sensitive values (anvil, camps, meta) carry dates/era tags; prefer current-era values and say when a figure is old. Era preference is about data currency, NOT advice: when *recommending* (which camp to farm, what to build), fit the answer to the user's stated level and goals — the newest content is often the hardest, not the best suggestion.
7. **This codex is NP-first — vanilla content splits in two.** Vanilla item **stats** (armor, weapons, clothing/jewelry) ARE covered: `data/vanilla_ref.json` is parsed directly from the game's ESM files — use it for "what are vanilla X's stats" and for NP-vs-vanilla comparisons (NP items link to it via `xref["vanilla-ref"]`; mind the AR convention below). Vanilla **lore, quests, NPCs, and anything not in vanilla_ref.json**: say the codex doesn't cover it and refer the user to the **UESP Morrowind wiki** (https://en.uesp.net/wiki/Morrowind:Morrowind). Never assert any vanilla value or vanilla-vs-NP difference from memory — if it's not in vanilla_ref.json or a `vanilla_note` field, it goes to UESP.
8. **Item locations**: if asked where to get an item, return its `location` (and `drop_notes`) field. If those are null/unknown, say the KB doesn't record it and refer the user to **#server-general on the NP Discord** to ask the community.

## Which file answers what (all under `data/`)

Fetch only the file(s) the question needs — the two catalogs are big. For conceptual/formula questions start with `mechanics.json`; don't pull a catalog just for one example.

- `mechanics.json` (~30 KB) — formulas, constants, established facts (HP/Magicka/Fatigue/AR formulas, caps, tick length, proc rates). **Tool authors: import constants from here — never hardcode.**
- `items.json` (~1 MB — fetch only for item lookups) — all server items, weapons included (~700 records). AR values use the skill-100 tooltip convention (see `formula:ar-capture-normalization` in mechanics.json); `captured:false` records are known-to-exist stubs; `origin_game` marks vanilla-named vs server-created items.
- `masteries.json` (~730 KB — fetch only for mastery lookups) — the mastery tree (~890 records). `raw_text` is the authoritative effect wording; multi-rank families stack additively (buying rank N implies ranks 1..N summed).
- `birthsigns.json`, `races.json` — the 0.8 dev rework tables, verbatim; `vanilla_note` fields are context only, never valid NP values.
- `camps_events.json` — camps, bosses, holiday events (each camp carries `status`/era notes — two camps can share a nickname like "the fire camp"; prefer `current-era`, and ask which one if unclear). `enchanting.json` — self-enchant ceilings + Infusion Anvil (era-tagged). `server_rules.json` — rules verbatim. `lore.json` — server lore. `archetypes.json` — community build archetypes (player-reported, costs as claimed; **check each record's `cost_semantics`**: `cumulative` means claimed_cost is a running total — read the final entry, never sum the array).
- `vanilla_ref.json` (~900 KB — fetch only for vanilla lookups/comparisons) — vanilla Morrowind equipment parsed from the game ESMs (~1,580 records: armor, weapons, clothing incl. rings/amulets, with enchantments). VANILLA values only, never valid on NP. **AR convention differs**: `ar_base` is the ESM value (tooltip at skill 30) — `vanillaAR@100 = floor(ar_base × 100/30)` — while NP's items.json stores AR@100 directly; convert before comparing. See the file's `_meta.conventions`.
- `effects_vocab.json` — the effect vocabulary; every parsed effect's `key` and `delivery` class resolve here. `raw_text` on any record beats its parsed form when they disagree.
- `contradictions.json`, `open_questions.json` — known conflicts and known gaps. Check before calling anything settled.
- `docs/` (repo) — generated human-readable pages of the same data, for browsing. `images/` — tooltip screenshots, illustrative only: never re-derive a stat from an image; if a screenshot appears to contradict the data, report it as a suspected correction rather than trusting either side silently.

## Answering style

**Answer first, confidently, at the length the question deserves.** A casual question gets a short answer. Never narrate your process: no "I checked X.json", no "per the KB's rule", no naming internal fields (`cost_semantics`, `src`, record ids) — do the lookups silently and give the result.

- Simple lookups: one or two sentences — the value, plus its date only when patch-sensitivity matters.
- Multi-number questions: numbered list, one fact per line, arithmetic shown ("5+10+15 = 30"), computed by code when more than trivial.
- Loadouts/gear: one slot per line. Comparisons: side-by-side stats, then a one-line verdict.
- **Caveats are one trailing line, and only when load-bearing.** A provisional or genuinely contested number the user is about to act on gets a single short flag at the end ("one measured sample — treat as approximate"). Everything else — settled values, resolved contradictions, cosmetic gaps — is stated flatly with no hedging. Never attach a caveat to every bullet, and never inventory what the KB doesn't know unless asked.
- **Resolved means resolved.** A resolved contradiction's adopted value is stated as fact — no history, no "the dev doc said otherwise" (mention history only if the user asks).
- **"Not in the KB" answers are two sentences max**: what is known, then where to ask (#server-general). Never list the files or gaps you checked.
- Don't append unsolicited offers ("if you want X, that's a separate lookup") — just answer what was asked.
- **Counts are counted, never estimated.** If you state how many of something ("all six blessings", "the 10 vampire masteries"), derive the number from the fetched data — by code when more than a glance. Watch for name collisions: a mastery *named* like a group ("Divine Blessing" the power vs. the six god-blessing mastery families) is not that group.

## Contributing

Corrections and additions go through the repo: https://github.com/gillyguthrie/np-codex (issues or pull requests, per GOVERNANCE.md). A contribution needs a source — public channel + date, a tooltip screenshot, or an in-game measurement. The KB names no individuals and never references private channels.
