# Nerevarine Prophecies Codex

The community knowledge base for the **Nerevarine Prophecies (NP)** TES3MP Morrowind server — every item, mastery, birthsign, formula, camp, and rule, machine-readable and AI-ready.

**The one thing to know: NP is not vanilla Morrowind.** Birthsigns, racials, item stats, and core formulas are server-custom. Values that feel familiar from vanilla or UESP are frequently wrong here — look them up.

- [What's in this repo](#whats-in-this-repo)
- [How to use Claude with this Codex](#how-to-use-claude-with-this-codex)
- [How to use ChatGPT with this Codex (untested)](#how-to-use-chatgpt-with-this-codex-untested)
- [Repo layout](#repo-layout)
- [Using the data programmatically](#using-the-data-programmatically)
- [Status](#status) · [Credits](#credits) · [License](#license)

## What's in this repo

Everything lives as JSON under `data/`, with per-fact provenance (source, date, confidence):

- **~700 server items** with stats, effects, and tooltip screenshots — plus a vanilla-Morrowind reference (1,584 records parsed from the game files) for NP-vs-vanilla comparisons
- **~890 masteries** (the full CM tree), **13 birthsigns** and **10 races** (the 0.8 rework tables)
- **Formulas and constants** — HP, Magicka, Fatigue, Armor Rating, caps, tick rates — validated against in-game measurements
- **Camps, bosses, and events**, **enchanting + Infusion Anvil** data, **server rules**, **lore**, and **community build archetypes**
- Honest bookkeeping: known **contradictions** and **open questions** are first-class records, not silent gaps

## How to use Claude with this Codex

You do **not** need to download this repo — just one small file.

1. Download **[np-codex.skill](https://github.com/gillyguthrie/np-codex/raw/main/np-codex.skill)** (one click; it's a few KB).
2. Open a chat with Claude (web, desktop, or mobile) and **attach the downloaded file**.
3. Claude will offer to **save it as a skill** — accept.
4. That's it. Ask anything about NP: *"What does the Atronach sign do here?"*, *"Compare Keening and Sunder"*, *"How much HP will my level 60 Nord have?"*

The skill fetches the data files it needs straight from this repo on every question, so answers always reflect the current version. The chat needs web access enabled — if Claude says it can't reach the web, that's the skill correctly refusing to guess from memory.

## How to use ChatGPT with this Codex (untested)

**Use Claude for best results** — the Codex is built and continuously tested against Claude, and the ChatGPT route below is **untested**: it may work since the skill is plain text with public data URLs, but nobody has verified its accuracy there. If you try it, double-check important numbers against the data files in this repo.

1. Open **[SKILL.md](SKILL.md)** in this repo and copy its full contents.
2. In ChatGPT (with web browsing enabled), paste it with a message like: *"Follow these instructions for any question about the NP Morrowind server."*
   - Or, for a permanent setup: create a **Custom GPT** and paste SKILL.md into its Instructions.
3. Ask your NP questions in the same chat — in principle it fetches the same live data files.

## Repo layout

- `data/` — **the authority.** All knowledge as JSON. Start with `data/mechanics.json` (formulas/constants), `data/items.json`, `data/masteries.json`.
- `data/vanilla_ref.json` — vanilla Morrowind equipment stats parsed directly from the game's ESM files, for NP-vs-vanilla comparisons. Vanilla values only — never valid on NP.
- `docs/` — human-readable reference, **generated** from `data/` (`python tools/generate_docs.py`). Never hand-edited.
- `images/items/` — audited tooltip screenshots, named by item id.
- `schema/` — JSON Schemas and data conventions.
- `tools/` — doc generator, structural validator, hygiene checks, effects audit, upstream-sync checker.
- `GOVERNANCE.md` — the rules that keep this KB trustworthy. Read it before contributing — or before building a tool on the data.
- `SKILL.md` / `np-codex.skill` — the AI assistant skill (see the two how-to sections above).
- `llms.txt` — machine-facing entry point for AI tools scanning this repo.

## Using the data programmatically

Every record has a stable `id` that never changes (display names can). Load-bearing values are `{value, src}` pairs resolving into each file's `sources` registry — or explicitly `{value: null, status: "unknown"}` when the KB doesn't know. Confidence tiers: `dev-stated` > `measured` > `player-reported` > `provisional` > `contested`. Check `data/contradictions.json` and `data/open_questions.json` before assuming an answer is settled.

Fetch raw files from `https://raw.githubusercontent.com/gillyguthrie/np-codex/main/data/<file>.json`. Import formula constants from `mechanics.json` — never hardcode them. See [`llms.txt`](llms.txt) for the full machine-facing guide.

## Status

Public release, migrated from a private research corpus built from the server wiki, public Discord channels, in-game tooltips, and in-game measurement campaigns (e.g. the armor-rating formula was validated against 18/18 in-game readings), then hardened through multiple rounds of simulated-user testing. Corrections welcome — see GOVERNANCE.md.

## Credits

Item data and tooltip images are cross-checked against and enriched by the [NP-Server-Items](https://github.com/Skooma-Breath/NP-Server-Items) community dataset by **Skooma Breath**, ingested with the author's permission. Run `python tools/ingest_upstream.py` to check that dataset for updates.

## License

Code (`tools/`, `schema/`) under MIT; data and generated docs (`data/`, `docs/`) under CC-BY 4.0. See `LICENSE`.
