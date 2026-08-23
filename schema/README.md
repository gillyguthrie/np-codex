# Schemas

Formal JSON Schemas are provided for the two largest files (`item.schema.json`, `mastery.schema.json`) plus shared definitions (`common.schema.json`). The remaining data files follow the same conventions and are structurally validated by `tools/validate.py`:

- Every data file is an object with a `sources` registry (`common.schema.json#/definitions/source`) and one or more record arrays.
- Every record has an immutable slug `id` (`type:slug`) and a `src` key resolving into `sources`.
- Load-bearing numbers are `sourcedValue`s: `{value, src}` or `{value: null, status}` — never a bare guess.
- Parsed effects reference `data/effects_vocab.json` keys and carry a `delivery` class; verbatim text is preserved in `raw_text`.

File map: `items.json`, `masteries.json`, `birthsigns.json`, `races.json`, `mechanics.json` (constants / formulas / facts), `camps_events.json`, `server_rules.json`, `enchanting.json`, `lore.json`, `archetypes.json`, `effects_vocab.json`, `contradictions.json`, `open_questions.json`.
