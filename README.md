# np-kb — Nerevarine Prophecies Knowledge Base

A community-maintained, machine-readable knowledge base for the **Nerevarine Prophecies (NP)** TES3MP server: items, masteries, birthsigns, races, formulas and mechanics, camps and events, enchanting, rules, and lore.

**The one thing to know: NP is not vanilla Morrowind.** Birthsigns, racials, item stats, and core formulas are server-custom. Values that feel familiar from vanilla or UESP are frequently wrong here — look them up.

## Layout

- `data/` — **the authority.** All knowledge lives here as JSON with per-fact provenance (origin, date, confidence). Start with `data/mechanics.json` for formulas/constants and `data/items.json` / `data/masteries.json` for the big catalogs.
- `docs/` — human-readable reference, **generated** from `data/` (`python tools/generate_docs.py`). Never hand-edited.
- `schema/` — JSON Schemas and data conventions.
- `tools/` — doc generator, structural validator, hygiene checks.
- `GOVERNANCE.md` — the rules that keep this KB trustworthy. Read it before contributing — or before building a tool on the data.
- `SKILL.md` / **[np-codex.skill](np-codex.skill)** — the np-codex AI assistant skill. **You don't need to download this repo to use the KB with an AI**: grab just the `np-codex.skill` file, open it in Claude, and save it — the skill fetches the data files it needs straight from this repo, so answers always come from the current version. **Not a Claude user?** The skill is plain text with public data URLs: open [SKILL.md](SKILL.md), copy its contents, and paste them into ChatGPT (as a message with "follow these instructions for NP questions", or into a Custom GPT's instructions) with web browsing enabled — it will fetch the same live data files and behave the same way.

## Using the data

Every record has a stable `id` that never changes (display names can). Load-bearing values are `{value, src}` pairs resolving into each file's `sources` registry — or explicitly `{value: null, status: "unknown"}` when the KB doesn't know. Confidence tiers: `dev-stated` > `measured` > `player-reported` > `provisional` > `contested`. Check `data/contradictions.json` and `data/open_questions.json` for known conflicts and gaps before assuming an answer is settled.

## Status

Initial public release, migrated from a private research corpus built from the server wiki, public Discord channels, in-game tooltips, and in-game measurement campaigns (e.g. the armor-rating formula was validated against 18/18 in-game readings). Item tooltip images are planned for a follow-up release. Corrections welcome — see GOVERNANCE.md.

## Credits

Item data and tooltip images are cross-checked against and enriched by the [NP-Server-Items](https://github.com/Skooma-Breath/NP-Server-Items) community dataset by **Skooma Breath**, ingested with the author's permission. Run `python tools/ingest_upstream.py` to check that dataset for updates.

## License

Code (`tools/`, `schema/`) under MIT; data and generated docs (`data/`, `docs/`) under CC-BY 4.0. See `LICENSE`.
