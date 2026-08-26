# Nerevarine Prophecies Codex

The community knowledge base for the **Nerevarine Prophecies (NP)** TES3MP Morrowind server — every item, mastery, birthsign, formula, camp, and rule, machine-readable and AI-ready. It also carries a full **vanilla Morrowind reference layer** (items, lore, books, NPCs, spells, locations parsed from the game files), so it can talk about the base game too — not strictly server stuff.

**The one thing to know: NP is not vanilla Morrowind.** Birthsigns, racials, item stats, and core formulas are server-custom. Values that feel familiar from vanilla or UESP are frequently wrong here — look them up.

- [What's in this repo](#whats-in-this-repo)
- [How to use Claude with this Codex](#how-to-use-claude-with-this-codex)
- [Repo layout](#repo-layout)
- [Using the data programmatically](#using-the-data-programmatically)
- [Status](#status) · [Credits](#credits) · [License](#license)

## What's in this repo

Everything lives as JSON under `data/`, with per-fact provenance (source, date, confidence):

- **~700 server items** with stats, effects, and tooltip screenshots
- **~890 masteries** (the full CM tree), **13 birthsigns** and **10 races** (the 0.8 rework tables)
- **Formulas and constants** — HP, Magicka, Fatigue, Armor Rating, caps, tick rates — validated against in-game measurements
- **Camps, bosses, and events** (era-tagged: old-server content is kept as history, never presented as live), **enchanting + Infusion Anvil** data, **alchemy** (vanilla ingredient baselines + NP customs), **server rules**, **server lore**, the **server timeline** (2018–present dev-announcement digest), and **community build archetypes**
- **Player services**: purchasable housing, the Login Points currency and its exchange, and the appearance systems (Dwemer Glamour Analyzer, passive robe/skirt endowment)
- **The vanilla layer**: equipment stats (1,584 records from the game ESMs), all 449 in-game books/notes summarized, storyline arcs and the great lore questions, 633 service NPCs, 1,065 spells, and item placements — for vanilla questions and NP-vs-vanilla comparisons
- Honest bookkeeping: known **contradictions** and **open questions** are first-class records, not silent gaps

## How to use Claude with this Codex

You do **not** need to download this repo — just one small file.

1. Download **[np-codex.skill](https://github.com/gillyguthrie/np-codex/raw/main/np-codex.skill)** (one click; it's a few KB).
2. In Claude, go to **Settings → Capabilities** and make sure **Code execution and file creation** is turned on.
3. Go to **Customize → Skills** and **upload the downloaded file** (this page also lets you toggle skills on and off). Alternatively, attach the file in a chat and accept when Claude offers to save it as a skill.
4. Invoke the skill by typing **`/np-codex`** followed by your question. Ask anything about the server — or the base game: *"What is a Rose of Renewal?"*, *"How can I best spend 200 mastery points as a lvl 30 mage?"*, *"Is Dagoth Ur a bad guy?"*

The skill pulls the data files it needs straight from this repo on every question, so answers always reflect the current version. The chat needs web access enabled — if Claude says it can't reach the web, that's the skill correctly refusing to guess from memory. Vanilla lore, items, and NPCs are fair game too — the codex answers those from its vanilla layer and points to UESP for anything beyond it.

## Repo layout

- `data/` — **the authority.** All knowledge as JSON. Start with `data/mechanics.json` (formulas/constants), `data/items.json`, `data/masteries.json`; `data/services.json` for housing/Login Points/glamours; `data/server_eras.json` for the timeline.
- `data/vanilla_*.json` — the vanilla Morrowind layer, parsed directly from the game's ESM files: `vanilla_ref` (equipment), `vanilla_lore` + `vanilla_lore_books` (storylines and all 449 texts, summarized), `vanilla_npcs`, `vanilla_spells`, `vanilla_locations`, `vanilla_processes`. Vanilla values only — never valid on NP.
- `docs/` — human-readable reference, **generated** from `data/` (`python tools/generate_docs.py`). Never hand-edited.
- `images/items/` — audited tooltip screenshots, named by item id.
- `schema/` — JSON Schemas and data conventions.
- `tools/` — doc generator, structural validator, hygiene checks, effects audit, consistency checker, upstream-sync checker, and the eval question bank the skill is tested against.
- `GOVERNANCE.md` — the rules that keep this KB trustworthy. Read it before contributing — or before building a tool on the data.
- `SKILL.md` / `np-codex.skill` — the AI assistant skill (see the how-to above).
- `llms.txt` — machine-facing entry point for AI tools scanning this repo.

## Using the data programmatically

Every record has a stable `id` that never changes (display names can). Load-bearing values are `{value, src}` pairs resolving into each file's `sources` registry — or explicitly `{value: null, status: "unknown"}` when the KB doesn't know. Confidence tiers: `dev-stated` > `measured` > `player-reported` > `provisional` > `contested`. Check `data/contradictions.json` and `data/open_questions.json` before assuming an answer is settled.

Fetch raw files from `https://raw.githubusercontent.com/gillyguthrie/np-codex/main/data/<file>.json`. Import formula constants from `mechanics.json` — never hardcode them. See [`llms.txt`](llms.txt) for the full machine-facing guide.

## Status

Public release, migrated from a private research corpus built from the server wiki, public Discord channels, in-game tooltips, and in-game measurement campaigns (e.g. the armor-rating formula was validated against 18/18 in-game readings), then hardened through many rounds of simulated-user testing against a growing eval bank. Corrections welcome — see GOVERNANCE.md.

## Credits

Item data and tooltip images are cross-checked against and enriched by the [NP-Server-Items](https://github.com/Skooma-Breath/NP-Server-Items) community dataset by **Skooma Breath**, ingested with the author's permission. Run `python tools/ingest_upstream.py` to check that dataset for updates.

## License

Code (`tools/`, `schema/`) under MIT; data and generated docs (`data/`, `docs/`) under CC-BY 4.0. See `LICENSE`.
