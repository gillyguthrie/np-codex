<!-- GENERATED from data/mechanics.json by tools/generate_docs.py — do not hand-edit. -->

# NP Mechanics — constants, formulas, facts

> NP is not vanilla Morrowind. Formulas and values here are server-specific; vanilla/UESP values are wrong on NP more often than right.


## Constants

| id | name | value | unit | note |
|---|---|---|---|---|
| `const:tick-length` | Regen tick length | **6** | seconds | Stopwatch-confirmed; supersedes the earlier ~7s community estimate. HoT/MoT/FoT effects tick every 6s. |
| `const:level-cap` | Character level cap | **60** | level | Attribute multiplier gains are server-controlled so all attributes max by 60. |
| `const:mp-cap-per-level` | Mastery points cap per level | **25** | points/level | 1500 total at level 60. Dev-stated accrual: all 1500 in roughly 44-46 days of logged playtime. |
| `const:hp-ratio-combat` | L60 effective HP ratio — Combat | **3.6** | HP/END | From the community HP calculator; NOT yet validated by direct measurement (Stealth and Magic ratios are). |
| `const:hp-ratio-stealth` | L60 effective HP ratio — Stealth | **2.8** | HP/END | Validated exact on an L60 character (100 END -> 280 HP). |
| `const:hp-ratio-magic` | L60 effective HP ratio — Magic | **2.2** | HP/END | Validated within 1 HP (observed 219 vs predicted 220; 2.2-vs-2.19 rounding open). |
| `const:hp-spec-mult-combat` | HP specialization multiplier (engine) — Combat | **1.14** | x | Dev-quoted engine script value. Relationship to the effective 3.6/2.8/2.2 ratios: the ratios fold in additional layers (see formula:hp). |
| `const:hp-spec-mult-magic` | HP specialization multiplier (engine) — Magic | **1.033** | x |  |
| `const:hp-spec-mult-stealth` | HP specialization multiplier (engine) — Stealth | **1.077** | x |  |
| `const:magicka-mult-atronach` | Fortify Maximum Magicka — Atronach (Wombburn) | **1.2** | x INT | In-game tooltip reads 1.2x verbatim; the 0.8 dev doc said 1.25x — see contradictions (tooltip adopted as truth). |
| `const:magicka-mult-mage` | Fortify Maximum Magicka — Mage (Fay) | **1.0** | x INT |  |
| `const:magicka-mult-apprentice` | Fortify Maximum Magicka — Apprentice (Elfborn) | **1.5** | x INT |  |
| `const:magicka-mult-altmer` | Fortify Maximum Magicka — High Elf racial | **1.5** | x INT | Validated in-game 2026-08 (exact fit in the flat-stack model). |
| `const:magicka-mult-breton` | Fortify Maximum Magicka — Breton racial | **0.5** | x INT |  |
| `const:int-cap-magicka` | INT cap in the magicka formula | **175** | INT | INT above 175 adds no magicka — and corrupts the pool (see fact:overmax-magicka-bug). |
| `const:fort-cap-default` | Default attribute fortification cap (L60) | **175** | pts | Attribute sheet clamps at 175 without a Fortification-Max mastery; raised per-attribute by such masteries. |
| `const:fatigue-level-bonus-l60` | NP fatigue flat bonus at L60 | **55** | pts | Validated exact on two independent L60 characters; +1 at L1; curve between unmeasured. |
| `const:dodge-penalty-magic` | Dodge chance penalty — Magic spec | **25** | pts |  |
| `const:dodge-penalty-combat` | Dodge chance penalty — Combat spec | **50** | pts |  |
| `const:cast-penalty-combat` | Cast chance penalty — Combat spec | **25** | pts |  |
| `const:cast-penalty-stealth` | Cast chance penalty — Stealth spec | **50** | pts |  |
| `const:accuracy-penalty-stealth` | Melee accuracy penalty — Stealth spec | **25** | pts |  |
| `const:accuracy-penalty-magic` | Melee accuracy penalty — Magic spec | **50** | pts |  |
| `const:ar-slot-weight-cuirass` | Sheet AR slot weight — cuirass | **0.3** | fraction |  |
| `const:ar-slot-weight-standard` | Sheet AR slot weight — helm/shield/greaves/boots/each pauldron | **0.1** | fraction |  |
| `const:ar-slot-weight-gauntlet` | Sheet AR slot weight — each gauntlet | **0.05** | fraction |  |
| `const:piece-ar-divisor` | Piece AR skill divisor | **30** |  | tooltip AR = floor(base AR x armor skill / 30) |
| `const:unarmored-coefficient` | Unarmored slot AR coefficient | **0.0065** |  | AR per empty/clothing slot = UnarmoredSkill^2 x 0.0065 |
| `const:healing-cap` | Healing spell cap | **100** | HP/second |  |
| `const:npc-training-per-day` | NPC training sessions per earth day | **5** | sessions | A 10/day player claim exists — see contradictions; the dev doc wins. |
| `const:cell-reset-hours` | Cell reset window (unloaded) | **3-6 hours** |  | 3-6 hours as long as no player has the cell loaded; stored as text because it is a range. |
| `const:magic-resistance-cap` | Magic resistance cap | **85** | % |  |
| `const:speed-cap` | Speed cap | **— (contested)** |  | 350 (2021 claim) vs 175 at L60 (2024 claim) — see contradictions; unresolved. |
| `const:melding-pct-per-rank` | Melding Construct AR bonus per rank | **4** | %/rank | PROVISIONAL — from a single item reading (+20% at rank 5). Applies to equipped-armor AR. |
| `const:anvil-armor-ar-multiplier` | Anvil max upgrade — armor piece AR multiplier | **1.54** | x | PROVISIONAL — one measured item pair (fresh 250 vs maxed 385 at matched skill/condition). A relayed '+42 AR flat' figure did not match — see contradictions. |
| `const:native-magicka-regen` | Native magicka regen | **1** | magicka/tick | For all characters EXCEPT Stunted Magicka (Atronach). Deliberate NP GMST edit. |
| `const:enchant-skill-one-charge` | Enchant skill for 1-charge casts | **110** | skill | At 110 Enchant, all enchanted items cost 1 charge per use (multiple corroborations 2019-2022). |
| `const:max-effects-per-enchant` | Max effects per enchant/spell | **8** | effects | Soul size raises magnitude/duration, never the effect count. |
| `const:vampire-daywalker-cost` | Daywalker perk cost | **50** | mastery points |  |
| `const:vampire-ancient-bloodline-cost` | Ancient Bloodline perk cost | **75** | mastery points | Requires Daywalker first; both together 125 points. |

## Formulas

### Max Health (L60 effective)  
`HP = floor(END x (spec_ratio + sum(health_factor_bonuses))) + flat_fortify_health`  
spec_ratio: see const:hp-ratio-*. Dev-stated structure: HP = Endurance x HP Factor(s) x spec multiplier + flat fortify; every character starts with 1 innate HP Factor; Health-Factor perks add on (+1 HP Factor -> 1 END = 2 HP). Endurance is retroactive/real-time. How +0.2-class Health-Factor mastery lines interact with the L60 ratio is OPEN (q:health-factor-stacking).

### Max Magicka (flat-stack model)  
`maxMag = floor(min(INT, 175) x (1 + sum(fortify_max_magicka_multipliers))) + flat_fortify_magicka`  
Base 1x INT for everyone. The ONLY xINT carriers: signs Atronach 1.2 / Mage 1.0 / Apprentice 1.5; racials High Elf 1.5 / Breton 0.5 (see const:magicka-mult-*). No specialization factor. Validated exact on an L60 character (mult 3.7: floor(125x3.7)=462; floor(175x3.7)=647). Items can also carry xINT multipliers. WARNING: in-game readings above the INT cap are unstable — see fact:overmax-magicka-bug. Spell Absorption/Reflect stack multiplicatively: total = 1 - prod(1 - each); resists stack additively.

### Max Fatigue  
`maxFat = STR + WIL + AGI + END + level_bonus`  
level_bonus: +55 at L60 (validated exact on two characters), +1 at L1; curve between unmeasured. One measured L60 character reads +126 above this model — same character carries an unexplained magicka surplus (q:hidden-passive-anomaly).

### Armor piece tooltip AR  
`tooltipAR = floor(baseAR x armorSkill / 30)`  
Verified for light/medium/heavy at skill 100 and (item-fortified) 118. NP base ARs deviate from vanilla (e.g. Daedric Tower Shield NP base 40 vs vanilla ESM base 80 — see data/vanilla_ref.json) — never take a vanilla base from memory or UESP; vanilla_ref.json is parsed from the game ESMs. [Correction 2026-08-23: an earlier version of this note said 'vanilla 45' — a memory-sourced error caught by the ESM extraction.]

### AR capture-skill normalization convention  
`AR@100 = floor(baseAR x 100/30); baseAR = tooltipReading x 30 / captureSkill`  
CONVENTION: all item AR values in this KB are stated at the skill-100 tooltip baseline (AR@100), independent of who captured them or at what armor skill. Any tooltip captured at a different armor skill MUST be normalized through this formula before entry. Screenshots posted publicly by unknown players may be at unknown skill — such values are marked 'as-posted tooltip, capture skill unknown' in the item record until verified.

### Unarmored slot AR  
`AR_per_slot = unarmoredSkill^2 x 0.0065`  
Skill 100 -> 65; empty or clothing-filled armor slots count at this value. Consequence: with high Unarmored, equipping a LOW-AR piece can lower sheet AR.

### Character sheet AR  
`sheetAR = floor(sum(slot_tooltip_AR x slot_weight)) [+ flat Shield effects + flat Armor Bonus masteries]`  
Slot weights: const:ar-slot-weight-*. Validated 18/18 exact across two characters at armor skills 100 and 118. Armor condition scales AR down as it degrades (confirmed). Piece AR at skill >100 from mastery cap-raises may scale non-linearly — open anomaly q:piece-ar-above-100. Tool authors: there is no enumerated registry of which masteries grant flat Armor Bonus — find them by searching masteries.json raw_text for 'Armor Bonus'; treat that list as player-curated until a registry exists.

### Dodge chance  
`dodge = sum(mastery_dodge_bonuses) - spec_penalty`  
spec_penalty: Magic 25, Combat 50, Stealth 0 (see const:dodge-penalty-*).

### Hit damage (best power attack)  
`hit = best_strike_max x (STR + 50) / 100`  
Vanilla-structure damage scaling adopted by community tools; matches observed play but not formally validated on NP. Condition and armor reduction also factor into damage dealt (vanilla structure, unverified on NP).

### Focused Strike proc chance (Lightning/Freezing/Fiery)  
`proc% = 0.30 x Agility`  
Expert player statement, adopted as working truth: the tooltip's '30%' corresponds to 100 Agility; 100% proc at Agility >= ~334; scales linearly (190 AGI -> ~57%). Not dev-stated; a one-time count-test would confirm.

### Effective encumbrance with Feather  
`effEnc = max(0, equipped_weight - sum(feather_effects))`  
All Feather sources subtract: mastery flat feather, AR-scaled feather, item/custom-enchant feather. Wearing armor does not itself slow movement/jumping — only total encumbrance does (player-tested).

### Multi-rank mastery stacking  
`total_effect = sum(effects of ALL owned ranks 1..N)`  
Dev-stated 'perks stack additively'. Buying rank N implies owning ranks 1..N and their summed effects.

### Crafting material cost by tradeskill level  
`cost_at_L10 ~= cost_at_L1 / 10 (rounded down); success chance -10% per level the recipe is above your skill`  
Dev-clarified example: an 88-spool level-1 recipe costs ~12-15 spools at level 10. Crafting above your level is allowed at higher cost and failure risk.

### Total XP per tradeskill level  
`L1:0 L2:32000 L3:254750 L4:668250 L5:1272500 L6:2067500 L7:3053250 L8:4229750 L9:5597000 L10:7155000`  
Cross-checked against actual level-ups by two independent testers; Tailoring confirmed on the same curve.

### Chain Combo chained-spell damage  
`chained = spell_damage x chain_multiplier x duration [x3 if trigger is Burning Slash]`  
Chain Combo multiplies the SPELL's damage; it ignores the weapon's own damage and damage-over-time. Multipliers by weapon type were systematically player-tested (e.g. 2H Spear ~19.9-23.5, 1H Axe 14, 2H Long Blade ~9.7-9.8, 1H Short Blade 7); roughly halved inside one tested dungeon.

### Potion weight  
`weight = floor(average(ingredient_weights))`  
2025 addition: any fish ingredient caps potion weight at 1, even when the fish contributes no used effect.

### Maximum spell cost castable at 100% chance  
`maxCost_fullFatigue = floor(2*skill + will/5 + luck/10 + specBonus - 80); maxCost_zeroFatigue = floor(2*skill + will/5 + luck/10 + specBonus - (4/3)*100)`  
specBonus = the spec's cast-chance CM perk value: Sorcerer +20, Channeler +40, mage specs +0, Combat -25, Stealth -50. Fatigue interpolates the constant between 80 (full fatigue) and ~133.33 (zero fatigue). Community-tool formula, not dev-stated; one corroborating public report (server-general 2025-03-23) treats Willpower as marginal for cast chance until ~98%+, consistent with the will/5 term.


## Established facts

- **np-not-vanilla**: NP deliberately rewrites vanilla values: birthsigns and racials fully reworked in 0.8, item base stats differ from vanilla/UESP, and core formulas are server-custom. Vanilla knowledge must never be substituted for a missing NP value.
- **restore-vs-tick**: Constant 'Restore Health/Magicka/Fatigue' effects apply per SECOND; 'over Time' (HoT/MoT/FoT) effects apply per 6-second tick.
- **atronach-stunted-regen**: Stunted Magicka (Atronach) removes the native 1 magicka/tick regen AND halves all mastery-gained HoT/MoT/FoT tick regen; item-granted regen is not halved.
- **atronach-drain** **[provisional]**: As part of the 0.8 Atronach rework, the sign carries a self Damage Magicka effect (5% of total maximum magicka) — dev-described as a slow drain 'unless you do something about it'. Whether the drain is still live in the current era is unconfirmed.
- **overmax-magicka-bug**: Raising INT above the 175 cap does not just waste points — it CORRUPTS max magicka, and the corrupted value re-rolls on every relog (swinging high or low). Dev-acknowledged as an open issue (Jan 2026) and community-confirmed (Aug 2026). Fixes: damage INT, unequip INT gear to get under the cap, or relog.
- **login-staleness**: Stat values displayed at login can be stale; equipping/unequipping any item forces a recalculation to the correct value. Formula-verification readings should be taken after an equip cycle.
- **enchant-no-passive-recharge** **[contested]**: Per the 0.8 dev doc, enchanted items no longer passively recharge and require filled soul gems — but multiple corroborated player reports describe skill-based natural recharge at high Enchant skill. Unresolved; see contradictions.
- **ce-enchant-rolls**: Post-0.8 player constant-effect enchants roll a random final magnitude between the chosen min and max (enchanter mastery and certain racials improve the odds); a later change reportedly sets outcomes to the average of the range. Enter ranges as 1-X, never X-X.
- **disenchanting**: The Disenchanting mastery extracts a player enchant using an empty black soul gem (which shatters), returning the item to its blank, re-enchantable state.
- **player-goods-no-npc-value**: Player-made potions and player-enchanted items have no gold value to NPC merchants; they can only be sold to other players.
- **potion-active-limit**: The number of potions active at once on a character is limited, scaling with Alchemy skill.
- **skills-not-potion-fortifiable**: Skills cannot be fortified by potions on NP; fortifying a skill requires a spellmaking spell or enchant.
- **fort-caps-masteries**: Attribute/skill fortification caps can be raised via masteries ('Fortification Max' lines and certain racials).
- **endurance-retroactive**: Endurance affects health in real time (retroactively) — no need to front-load END early.
- **death-penalties**: On death: revival at the bound Spirit Master (or Seyda Neen), loss of some carried gold, and Mastery Point debt that halves mastery XP gain until paid.
- **respec-paths**: Mastery refunds are available via Rehabilitator Anja (Vivec, near the bank). Additionally, all level-60 players can respec once for FREE with Socucius Ergalla after completing the tax quest, provided zero CM points are currently spent; being online during the NP anniversary event granted one extra respec. Whether these are one mechanism or two is unresolved.
- **birthsign-change**: Birthsigns can be changed at the Census and Excise Office in Seyda Neen: first change per character free, subsequent changes via anniversary certificates. Whether purchased birthsign-gated masteries refund on change is open.
- **soultrap-summons**: Soultrap does not work on summoned creatures.
- **quest-no-trade**: Quest-tagged items cannot be sold to merchants; No-Trade-tagged items additionally cannot be traded to other players. Neither crosses accounts.
- **merchant-sync**: Since 0.8, merchant inventories and gold are synced across all players (an engine change), restocking after a few in-game days and resetting on server resets.
- **server-reset**: The server resets daily at 06:00 server time; cells reset 3-6 hours after being unloaded. NPCs killed are restored by resets.
- **training-limit**: NPC training is limited to 5 sessions per earth day (dev doc). A 10/day claim circulates — see contradictions.
- **autoban**: A scripted auto-ban system exists: leveling any skill too fast (threshold unknown), and picking up or dropping ~1 million gold at once, are confirmed triggers; it can also catch illegitimately-obtained items without a report.
- **pvp-flag**: PVP is opt-in via a toggle flag; hitting another player force-enables yours; killing unflagged players carries penalties including in-game prison. Honor kills earn tokens for custom PVP items; some items require the PVP flag to equip.
- **spec-terminology**: The Combat/Magic/Stealth axis is called 'specialization' (it drives mastery trees, specialization penalties, master classes, and equipment gating). 'Affinity' is the narrower subclass tag on certain masteries (e.g. Paladin/Wizard/Bard-class locks). The sheet's 'Class' name is player-authored and mechanically irrelevant.
- **full-set-side-effects**: Certain masteries grant AR-scaled side effects gated on a FULL armor-class set — all 8 body slots (helm, cuirass, greaves, boots, both pauldrons, both gauntlets) in that class, no off-class armor; a worn shield must match, an empty shield slot is allowed. Known: full Light -> Chameleon; full Medium -> Attack; full Heavy -> Feather; full Unarmored (no armor) -> Resist Magicka; gauntlet-scaled fist damage has no full-set requirement.
- **weakness-stack-multiplayer**: Combining Weakness-to-X with damage in one multi-effect spell multiplies damage beyond sequential casting, and stacking Weakness from MULTIPLE players exceeds the solo cap — dev-confirmed unintended ('not much I can do to resolve it for now').
- **weapon-speed-classes**: Confirmed tooltip weapon speeds: daggers 250-270%, longblades 125-150%, staffs 175%, 2H/spears ~100%. Reach: ALL 1H blades 6 ft (longblades have no reach advantage over daggers); 2H hammers/axes ~8.4-9.6 ft; spears and long staffs 10.8 ft.
- **glorious-tides**: Glorious Tides tier 3 at max Restoration heals 625 HP to caster and nearby group members (~1088 every 12s per caster with all tiers stacked; two healers rotating -> 1088 per 6s); simultaneous casts on one target do not stack — rotate casts. Hits up to 4 players, cannot target enemies.
- **cure-school-reclassification**: Adding a Cure effect to a custom spell reclassifies the whole spell as Restoration regardless of other effects (community-tested extensively) — enabling cheap casting of multi-school spells by training only Restoration. Cast chance for multi-school spells otherwise follows the effect with the lowest cast chance, which also sets the displayed school tag.
- **leveled-loot**: Leveled loot/creature spawn lists are determined by whichever player first enters the cell — except spawned creature camps, which are fixed. Displayed item drop rates don't always match observed rates (dev-stated).
- **bedrolls**: Free waiting-to-heal is disabled; all players start with a placeable bedroll usable in temples or player homes (crouch-activate to pick it back up).
- **character-limits**: Max 10 characters per player, max 4 played simultaneously (server rule 9).
- **custom-item-ids**: Every player-created custom item's internal ID begins with the prefix '$custom_'.
- **stat-caps-base**: 100 is the highest base stat value; 'Max' masteries raise the fortification ceiling above the default cap (see const:fort-cap-default). The /cs command shows current caps in-game.
- **fall-damage**: 1 point of Slow Fall negates all fall damage; fortifying Acrobatics to ~126+ is also reported to negate it.
- **jump-teleport-momentum**: Casting Almsivi/Divine Intervention or Recall right after a strong Jump carries momentum through the teleport (both directions) — the basis of long-distance jump travel.
- **skill-check-structure**: Most skill checks are roughly Skill + 20% of the governing attribute + 10% of Luck (player-reported). Running speed ~ Athletics x Speed with race/encumbrance modifiers; Levitate speed = Levitate magnitude + Speed, no Athletics.
- **beast-feet-slot-bug**: A login bug unequips beast-race characters' feet-slot gear; workaround is an /es equipment set hotkeyed at login. Avoid life-critical enchants on the feet slot for beast races.
- **enchanted-tools-bug-fixed**: Enchanting an axe/pickaxe used to stop it harvesting/mining; dev-confirmed bug, fixed Aug 2022. Two-handed weapons chop/mine better than one-handed (dev-stated); a Fortify Axe effect while mining can raise ore yield per node.
- **potion-active-limit-values**: The active-potion limit is 5 at Alchemy 100. The Cowl of the Druid raises the wearer's limit by 1, to 6 — it is the only item in the KB with this effect. Below Alchemy 100 the limit is lower (scales with skill); the exact curve is not recorded (q:potion-limit-curve).
- **potions-per-combine**: A fully equipped player alchemist gets 5 potions per combine.
- **potion-effect-caps**: Player-made potion magnitudes and durations are capped server-side: a maximum brewable value per effect exists ('maxed potions'). Elemental shield, resist, and fatigue effects escaped the across-the-board potion cap pass. Potions brewed before the cap pass ('pre-nerf' batches) persist in circulation and can exceed current brew ceilings.
- **potion-strength-inputs**: Potion strength scales with Alchemy skill first, then Intelligence, then Luck; skipping any max-investment source (racial line, Godborn) docks roughly 1 point of potion strength each. Current-era max-potion meta: Breton or Altmer, maxed Alchemy/INT/Luck, Metabolist master class, full Secret Master apparatus set.
- **ingredient-eating-first-effect**: Eating an ingredient raw grants only its first-listed effect.
- **vampire-dust-vampirism-cosmetic**: The Vampirism effect on Vampire Dust changes the drinker's appearance only; it carries none of the actual vampirism scripting.
- **mass-brew-caution**: Very large single combines are risky: a 1000-potion combine triggered the server's anti-cheat auto-ban, and mass brewing lags the server. Community practice is roughly 100 potions per combine with a few seconds between batches.
- **alchemist-cm-budget**: A max-potency alchemist build was publicly accounted at ~950 CM: ~500 in base lines (Curiosity, max INT/Luck/Alchemy plus filler), 200 Metabolist master class, 75+75 for its two master-class abilities, and 100 Godborn.
