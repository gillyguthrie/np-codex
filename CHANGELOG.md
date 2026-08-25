# Changelog

## 2026-08-25 — v0.4.11 Enhancement effect settled: flat Armor Rating
- **The server-custom "Enhancement N pts" item effect adds N flat Armor Rating while equipped** — settled from three independent public statements found in a Discord sweep (2025-12-21: an owner read +50 AR from Enhancement 50; 2026-08-03: "Enhancement adds those raw numbers to your rating"; 2026-08-14: "adds 30 points of Armor", with the display quirk that the sheet updates only after reopening the inventory). effects_vocab note upgraded from "mechanics unknown"; new `fact:enhancement-effect` (player-reported). One report ties swapping Enhancement gear to armor-skill display fluctuation — possible under-the-hood implementation via armor-skill fortification, noted without changing the player-verified flat-AR outcome.
- Frost Etched Belt gains its chat-attested `Enhancement 30 pts` effect (tooltip screenshot still wanted); the other five carriers (Murk Claw Ring, Martial Band, Belt of Fish Scales, Glowing Heroic Band, Rune Etched Choker) already had it captured.
- Eval bank +1 (eq:043 — the "what does Enhancement do" probe).

## 2026-08-25 — v0.4.10 rank semantics corrected: increments STACK (v0.4.9's running-total ruling reversed)
- **The v0.4.9 running-total reading was wrong and is reversed, on community-measured evidence surfaced by a Discord-trove sweep**: a player's documented mastery-only Strength (~330 with no gear, "overmaxed by 10") is arithmetically unreachable under running totals but lands correctly under summing; a second player annotated "Combat Readiness 1/2/3 +10 str/speed fort max (each rank)". **Ruling: each rank's stated magnitudes are increments that stack — owning ranks 1..N sums every rank's values.** Costs and 500-gate semantics unchanged.
- **Shadowstalker's critical-strike-damage % is the ruled exception: Mug-style replacement** — the highest owned rank's % applies (rank 3 = 90%, rank 5 = 150%), never the sum.
- **Granted-actives behavior recorded** (dev-stated 2026-01-04, server-general): some ability families replace the previous tier (Mug), some grant coexisting abilities (Focused Strike; the 2026 Combat CMs intentionally don't overwrite). Actives never enter passive stat math.
- masteries.json `_meta.conventions` rewritten; SKILL.md file map + Playbook restored to summed semantics with the crit exception stated flatly; `np-codex.skill` repackaged.
- **Builder v1.22**: the v1.21 fx delta conversion reverted (fx again carry each rank's stated values; the summing engine is correct as-is). v1.21's other fixes retained: bare-"Max" cap parsing (Stealth Archer), race/sign fx label completions, Ancient Shrouded glove dedup. pub data.json `_meta.rank_semantics` states the stacking rule + crit exception for build agents. Playwright-verified: charbuild5 loadout loads clean, Deadeye 1–3 shows +6/+60 again, zero pageerrors.
- Eval bank +1: eq:042 (rank stacking + the crit exception as the regression probe); eq:039 notes corrected.

## 2026-08-25 — v0.4.9 rank step-up ruling + shield-slot unarmored engine-confirmed
- **RANK STEP-UP SEMANTICS (maintainer-ruled): multi-rank families' per-rank stated magnitudes are RUNNING TOTALS, not additions** — Shadowstalker 3's "+90% crit damage" is 90% total, never 30+60+90. Applies to every escalating sequence (+1/+2/+3 skill, 15/20/25 Fort. Max, 4/6/8 resist, crit %); identical repeated magnitudes ("Adds Passive: Feather +15" each rank) remain per-rank additions; costs always sum. Encoded in masteries.json `_meta.conventions`; SKILL.md file map + Playbook rewritten (builder fx are pre-converted deltas so fx-summing stays correct; raw-text-only magnitudes take the highest owned rank). Surfaced by charbuild5's flagged crit assumption — the decide-once rule working as intended.
- **Builder v1.21 ships the ruling**: build.py converts every strictly-monotonic per-rank fx sequence to deltas (122 family.key sequences, incl. negative step-downs like Tactician Str −5/−10), so the existing summing engine now yields exactly the rank-N stated totals. Also fixed: bare trailing "Max" now parses as Fortification Max ("+10 Sneak/Marksman Max" was adding +10 flat Sneak — Stealth Archer fx corrected to sneak 5/marks 5/caps 10/10 per rank); races/signs fx completed from their own labels (Bosmer Sneak +10 — caught live by charbuild5 — Khajiit Acro/H2H, Nord Axe, Redguard Feather, Thief Security, Steed Athl/Feather, Lady Speechcraft, Apprentice Feather); Ancient Shrouded glove duplicate pair removed. Playwright-verified on the community page: charbuild5's loadout loads clean, poison 149% capped at 85, zero pageerrors.
- **Empty-shield unarmored ruling (maintainer-questioned, settled from engine source)**: OpenMW's getArmorRating gives EVERY slot not holding an armor item — the shield/carried-left slot included — the unarmored rating 0.0065×skill² at its slot weight; UESP Combat concurs. formula:unarmored-ar note now states this explicitly; SKILL.md build-flow AR step tells agents to include it (charbuild5 omitted it).
- Ancient Shrouded glove AR is now an OPEN discrepancy: the wiki tooltip reads 46, a second in-game capture reads 49 (capture skill unknown), codex curated value 46.5 — builder carries 46 pending the capturing character's Light Armor value to normalize the 49.
- eq:039 regraded A (charbuild5: ~8 min, 33 calls, first complete delivery incl. inline JSON — maintainer-confirmed; every slot/owner/mastery/weapon validated).
- `np-codex.skill` repackaged.

## 2026-08-25 — v0.4.8 build-flow speed pass (inline JSON + one-catalog)
- **The loadout JSON is now delivered INLINE in the chat message, always**: the fenced .nplb.json code block IS the deliverable; the downloadable file is a bonus, never the only copy. Three of four blind stress-test runs lost the file to the platform's ~50-tool-call turn cap because the write was saved for last — an inline block can't be eaten.
- **One-catalog rule**: builds resolve every item, weapon, mastery, race, and sign against the builder's `data.json` ONLY (codex `mechanics.json` for formulas/caps, `enchanting.json` for self-enchant ceilings); the codex catalogs are off-limits during builds — two-catalog reconciliation was a recurring rabbit hole with zero accuracy payoff.
- **Default build download slimmed 8 → 3 files** (subsumed by the one-catalog rule). Call budget tightened to match: ~15 → ~10 calls, file-write deadline ~call 18 → ~12, hard research stop call 25 → 20.
- **Decide-once rule** added to the Playbook: ambiguity gets one defensible reading and ONE flagged line ("assumed X"), then move on — never multi-interpretation self-debate (round 4 argued the stacking question three ways before v0.4.7 settled it).
- **Continuation protocol**: a force-capped turn must end with "Say **continue** for the full build" — never a status report with no path forward.
- `np-codex.skill` repackaged.

## 2026-08-25 — v0.4.7 stacking rules settled + Atronach 1.25 scrubbed
- **`fact:stacking-rules` (maintainer-ruled): everything in the game stacks FLAT ADDITIVE except exactly two effects — Spell Absorption and Spell Reflect, which stack multiplicatively.** Sanctuary is additive and is NOT Spell Absorption — never fed into the absorption roll. Prompted by round-4 stress test (eq:040, graded C+): the assistant folded Sanctuary masteries into the multiplicative absorption math, producing "~74.5%" where the true figure (Atronach 15 + Necromancer's Amulet 25, the only real absorb sources) is 36.25%. formula:absorb-reflect-stacking note scoped; effects_vocab gains a binding stacking convention plus per-key stacking fields on absorb/reflect/sanc; eq:041 added as the regression probe.
- **Stale Atronach 1.25 scrubbed everywhere**: birthsigns.json raw_text now states 1.2 with the dev-doc 1.25 relegated to a bracketed historical note (the parsed magnitude was already 1.2); server_eras' historical 1.25 patch-note entry annotated as superseded; builder data corrected (signs.Atronach.magmult 1.25 → 1.2) and its legacy unused `magK` field deleted (builder v1.20). The 1.25 now exists only as dated history inside c:atronach-magmult, where it belongs.
- Round-3 blind test (eq:039, graded B): fetch discipline and honesty fixes all held — batched download first, zero web searches, level gates respected, Windshear correctly ruled out from damage-type data with its class stated as unrecorded — but the run hit the platform's ~50-tool-call turn ceiling with the chat build delivered and the .nplb.json NOT delivered (second consecutive file miss, both from saving the write for last).
- **SKILL.md: the file write now comes BEFORE the polish, no later than ~call 18** (chat text is free; the file costs a call; platform turns hard-stop near 40-50), and the call-25 stop rule now explicitly sequences: write the file immediately, then deliver.
- **SKILL.md: known-schemas block** for builder data.json and mechanics.json so agents stop spending ~10 calls per run inspecting file structures the skill can simply state.
- `np-codex.skill` repackaged.
- **SKILL.md build flow hardened from a live Sonnet stress test that ran out of tool budget with no deliverable**: explicit fetch-failure protocol (immediate curl fallback when the URL tool fails on raw.githubusercontent; NEVER web-search for the repo — nothing is indexed) and a hard call budget (one batched download of all needed files, 3-5 comprehensive analysis scripts, deliverable by ~15 calls; at call 25 stop researching, convert unresolved points to stated assumptions, and deliver the full two-format build).
- **Vampirism enters the public KB** (matching the model the community builder already ships): `fact:vampirism-passives` (+20 Agi/Str/Wil/Spe, +30 to eight skills, Para 100, Disease 100, NW +50, Weakness Fire 50; the old "+50 skills" reading was a Berne character — base+clan) and `fact:vampire-clan-bonuses` (Aundae/Berne/Quarra: +20 to one attribute + a three-skill trio; community-reported 2020-11, maintainer-confirmed 2026-08-24). The stress test had wrongly concluded clans were flavor-only because the KB was silent.
- **`const:nw-resist-cap` = 100 (provisional, maintainer-ruled)**: Resist Normal Weapons caps at 100, not 85 — full immunity is an in-game mechanic ("your weapon has no effect" on 100-resist creatures); additive stacking like all resists (only Absorption/Reflect are multiplicative). `const:magic-resistance-cap` note scoped to the magic resists.
- Builder data now carries **`wskill` weapon-skill tags** (v1.18: vanilla_ref-joined where matchable, name-heuristic provisional otherwise, null = untyped — 94/149 typed); SKILL.md playbook documents the field so agents stop name-guessing weapon classes.
- Eval bank +1 (eq:038 — the orc/vampire/heavy stress scenario, graded C on the pre-fix run). `np-codex.skill` repackaged.
- **Overmax is cap-relative, not flat-175 (maintainer-ruled 2026-08-24).** `fact:overmax-magicka-bug` rewritten: the corruption applies only when INT exceeds the character's EFFECTIVE cap (175 base + Intelligence Fortification Max mastery bonuses); an INT-181 character with a 260 cap had been mislabeled overmaxed. New `fact:overmax-system`: overmaxing covers attributes AND skills, threshold = base cap + that stat's Fortification Max (dev patch notes 2023–2026: drain-effect handling, /inspect shows overmaxed values, werewolf quirks).
- **Magicka scales with INT past 175 when the cap is raised.** `formula:magicka` now uses `min(INT, INT_cap)` with `INT_cap = 175 + sum(Intelligence Fortification Max)`; `const:int-cap-magicka` reframed as the un-raised BASE cap. The 2026-08-21 flat-cap reading is recorded and resolved in new contradiction `c:int-magicka-cap-flat-vs-raised` (attributed to that session's unstable pool readings).
- **"500 Points Spent" gate semantics settled** (masteries.json `_meta.conventions`, maintainer-stated): the gate counts points already spent on OTHER masteries — a gated mastery's own cost never satisfies its own gate (500 + 200-cost master class = 700 total); spent is a lifetime total, so one gated purchase counts toward later gates.
- **SKILL.md build flow reworked from live user feedback**: chat + file are BOTH delivered by default (the format question is gone); builder data is fetched from `raw.githubusercontent.com/gillyguthrie/np-character-builder/main/data.json` (the github.io URL 403s for agents — no more trial-and-error); "all magic resistances" defined as the six (Magicka/Fire/Frost/Shock/Poison/Paralysis, disease + normal weapons excluded); gear step sweeps EVERY slot with the zero-AR clothing rule (gloves ≠ gauntlets, shoes ≠ boots) and suggests labeled self-enchant fillers where the catalog is empty; chat builds get a name + short strengths/weaknesses/how-to-play blurb; new **Playbook** block (mastery section map, 500-gate semantics, one-pass planning, slot list, resist cap) to cut the observed 10-minute schema-rediscovery loop.
- `np-codex.skill` repackaged.
- Author-confirmed: Chronicles Volume II is "The Solstheim Weekend Massacre" — an in-world account of the 0.7 era's Solstheim closure. First two pages transcribed from a screenshot of the in-game tome into lore_texts.json (status: partial, three [name withheld] redactions pending authorization); the Chronicles lore entry updated. Remaining pages pending screenshots.

## 2026-08-24 — v0.4.3c gondolier full text
- lore_texts.json +1: The Gondolier of Balmora stored verbatim per maintainer call (7 texts now). On the full read, the closing "lesson" is bawdy in-world humor from an unreliable narrator (vanilla-Morrowind-style); the record's note says so explicitly, and the lore.json paraphrase entry was corrected (the story concludes with that mock moral — it is not an unfinished cliffhanger). Chronicles Volume II: searched the maintainer's Google Drive and the tes3mp folder — manuscript not found; only the in-game tome remains as a source.

## 2026-08-24 — v0.4.3b gondolier paraphrase + parody songs described
- lore.json +2: `lore:gondolier-of-balmora` (the unfinished May 2020 two-chapter story, paraphrased per maintainer call — on inspection it is scene-setting and a player-kill retelling, not the rough humor first flagged) and `lore:community-parody-songs` (the Jiubsmas carol and the 2020 mafia-initiation piece, described not stored — their lyrics are near-verbatim rewrites of real copyrighted songs). Chronicles Volume II noted as absent from the channel export (announced 2020-04-24, distributed only in-game).

## 2026-08-24 — v0.4.3 verbatim lore texts
- **New `data/lore_texts.json`** — six community-authored in-world texts stored VERBATIM for exact read-back on request: 36 Lessons of Horky Vol. 1, The Origin of Horky (Chronicles Vol. III), The Origin of Guars, The Magic Fork (Chronicles Vol. I), The Milkman farewell, and the School of the Arcane and the Unseen founding note. Read-back is always labeled community fiction; attribution is null on every text until the maintainer records authorization; two single-name redactions (`[name withheld]`) pending that authorization. Held out for a maintainer call: the gondolier story and two parody songs of real-world tunes. SKILL.md file map +1; eq:034; `np-codex.skill` repackaged.

## 2026-08-24 — v0.4.2d 0.8-only default frame
- **SKILL.md rule 6 hardened: the current 0.8 server is the ONLY default frame.** 0.7-era content (pre-2022-05-13 — old systems, Nerevarine Tokens, old racials/birthsigns, retold history) is never volunteered, mixed into a current-server answer, or used as padding; it appears only on an explicit history/0.7 question, plainly labeled as 0.7-era history. Matching lore.json `_meta` convention added; eval eq:033; `np-codex.skill` repackaged.

## 2026-08-24 — v0.4.2c tables for all structured answers
- **SKILL.md answering style: tiers, drop tables, cost breakdowns, comparisons, and any parallel records now render as markdown tables** (header row, one record per row, natural sort) — never comma-packed paragraphs; bullets only for ~2–4 one-dimensional items. Prompted by a real Heart's Day tier answer that shipped as an unreadable paragraph. Eval eq:032 added; `np-codex.skill` repackaged.

## 2026-08-24 — v0.4.2b era anchoring + two dev-stated mechanics facts
- **lore.json: new entry `lore:07-to-08-transition`** — the server's key historical dividing line: 0.7 era 2018-11-12 → storyline finale 2022-02-06; 0.8.1 launched 2022-05-13 as a fresh start (new characters, reworked racials/birthsigns, tradeskills). `lore:token-currency-origin` era-anchored: Nerevarine Tokens launched 2019-07-27, dev announcements about them span 2019–2021 with none after the 0.8 launch, and they are NOT used on 0.8 (maintainer-confirmed 2026-08-24); a community-misdated "2020" recollection corrected against the dev announcement record. New `_meta` convention: np-server-lore retold history is predominantly 0.7-era — never assume a 0.7 system exists on 0.8. New sources `updates-dev`, `maintainer`; eq:031 expectation strengthened with the era framing.
- **mechanics.json: two dev-stated facts from the np-server-lore channel** (new source `s-lorechan-dev`): `fact:invis-crit-limiter` (2022-11-01 — a custom mechanic intentionally limits invisibility-crit spam) and `fact:sujamma-vs-player-potions` (2022-11-30 — mastery-invested player potions far exceed Sujamma overall: Sujamma +50 Str/−50 Int nets zero, vs a debate-example potion at +98 attributes, +140 Fortify Health, +61 disease resist, +10s durations, no negatives).

## 2026-08-24 — v0.4.2 np-server-lore ingest + chat-build tables
- **lore.json: +18 entries** from the np-server-lore channel export (2020-04 → 2026-06): real server history (Token currency origin, the first Tradehouse, the gold-duplication purge, the first Jiubsmas, a predecessor server, the player note-board origin, the Balmora atronach siege, Heddvild "the Undying", the Pelagiad "curse") and clearly-labeled community fiction (the Cult of Horky, the guar creation myth, the School of the Arcane and the Unseen, the Milkman legend, the Chronicles anthology, the dev-persona "Godhead" theory). Four new sources (`lorechan-anecdote`/`-dev`/`-fiction`/`-speculation`); `_meta.conventions` fiction firewall — `lorechan-fiction` content is always presented AS community fiction, never as server fact; no person names anywhere.
- **Chat builds are now tables** (UX): Masteries (mastery | ranks | cost, with a total-arithmetic row), Gear (slot | item | key stats), Targets (target | achieved | how), then the linked file offer. Quantitative stipulations are verified with KB formulas at a STATED armor-skill assumption, and FILE deliveries must set the state's `skl`/`skm`/`skh` to that same assumption so the builder's tiles reproduce the arithmetic.
- Dual-path acceptance test (orc battle mage, 900 CM, fire resist >85, AR ≥300): chat and file paths ran from the same SKILL.md flow + builder data (builder repo verified logic-free), both caught the Lord sign's fire weakness against the resist stipulation, file loaded live with Fire 105% and AR ≥ target (eq:030; lore probes seeded as eq:031).
- `np-codex.skill` repackaged.

## 2026-08-24 — v0.4.1b chat builds + builder discovery
- Build requests now offer BOTH deliveries: a readable chat build (race/sign/spec line, numbered masteries with cost arithmetic, gear one slot per line) or the builder-loadable file — asked as part of the single question round, ALWAYS with the builder's link and a one-phrase intro so users discover the tool. Chat builds use the same data and validation, so they remain exactly convertible to a file on request. Acceptance-tested (eq:029). `np-codex.skill` repackaged.

## 2026-08-24 — v0.4.1 loadout authoring for the community builder
- **SKILL.md: new "Building loadout files" section** — on an explicit build request, the codex fetches the builder's own data.json (published with builder v1.16), asks ONE compact round of fill-in-the-blank questions (birthsign, spec, named gear), selects masteries to the CM budget with arithmetic shown (prerequisite ranks included), picks gear from the builder catalog, validates every reference (byte-exact race/sign keys, weapon index, name|owner slot refs, exact mastery names), and delivers a .nplb.json the builder's Load button accepts. `np-codex.skill` repackaged.
- Acceptance-tested end to end: a "900 CM Dark Elf fire mage, daggers, heavy armor" request produced an exact-900 build that loaded into the live page with zero errors (eval bank eq:028).
- Companion builder release v1.16 (separate repo): duplicate clear-all id bug fixed (canceled reset no longer wipes masteries; panel clear-all now works), restore() guarded against unknown race/sign in hand-edited files, and pub/data.json now ships — the anonymized builder data as standalone JSON, extracted from the leak-scanned page.

## 2026-08-24 — v0.4.0 eval round 2 + storyline wording
- Persona eval round 2: 14 questions (7 regression, 7 fresh probing v0.3.1/v0.4.0 content) — 14/14 grounded, contested potion-limit handled per c:active-potion-limit, locations/NPCs/spells/eras files all exercised correctly. Eval bank grown to 27 questions; eq:003 expectation amended to the contested state.
- server_eras.json: two storyline entries reworded (the 0.7 finale's protagonist described as the server dev's in-world persona).

## 2026-08-24 — v0.4.0 dev-announcement ingest (server-updates channel)
- **New `data/server_eras.json`**: the server timeline — 29 era markers (launches, wipes, system reworks, 2018-2026) plus a 400-entry structured digest of every substantive dev announcement, with stated values preserved. Dev-stated tier; new `s-updates` source. This anchors every era tag in the KB.
- **Dev-stated upgrades**: fact:potion-effect-caps now cites the 2022-11-12 rework announcement (+ the 2024-08-06 reflect/absorb potion nerf); ench:roll-mechanics confirmed (min/max -> flat average, announced example 10-30 -> 20/20); new facts: spec HP/Magicka factors (2.4/1.6/1.0 and 0.9/1.15/1.5 — reconciling EXACTLY with measured 3.6/2.8/2.2 via a +1.2 base), quickkey potion ban, potion limit clears on death.
- **New enchanting facts**: the Enchantment Imprinting system (2026-01-15: 10 Gem Dust = 1 EV, Shard of Enchanting, 260 EV imprint cap), the Endowment System (2024-02-18, dev-stated), disenchanting requirements (Enchant 100, level 25).
- **New contradiction c:active-potion-limit**: dev 2019 curve says 6 at Alchemy 100+ (3/4/5/6); current-era player consensus says 5 (+Cowl -> 6). Unresolved — one in-game count settles it. q:potion-limit-curve and q:np-soul-rework updated with the dev-stated context.
- SKILL.md file map +1; `np-codex.skill` repackaged.

## 2026-08-24 — v0.3.2 maintainer infrastructure
- **New gate: `tools/check_consistency.py`** (gate 5) — cross-file reference checks: storyline tags resolve, storyline key_books exist, items.json vanilla-ref xrefs point at real vanilla_ref records, trainer/skill-book names are valid skills, camp tables agree, community_resources well-formed (URL liveness with --online).
- **New `tools/eval_questions.json`** — standing persona-eval question bank (17 questions seeded from the 2026-08-23 alchemy and lore evals, with expectation keys). Grown-only: every future eval appends its fresh questions; old ones are the regression net.
- `schema/README.md` file map refreshed: all 8 vanilla-baseline files documented, np_override convention and rule-9 binding noted.

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
