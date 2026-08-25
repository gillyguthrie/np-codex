<!-- GENERATED from data/mechanics.json by tools/generate_docs.py — do not hand-edit. -->

# NP Mechanics — constants, formulas, facts

> NP is not vanilla Morrowind. Formulas and values here are server-specific; vanilla/UESP values are wrong on NP more often than right.


## Constants

| id | name | value | unit | note |
|---|---|---|---|---|
| `const:tick-length` | Regen tick length | **6** | seconds | Stopwatch-confirmed; supersedes the earlier ~7s community estimate. HoT/MoT/FoT effects tick every 6s. |
| `const:level-cap` | Character level cap | **60** | level | Attribute multiplier gains are server-controlled so all attributes max by 60. |
| `const:mp-cap-per-level` | Mastery points cap per level | **25** | points/level | 1500 total at level 60. Dev-stated accrual: all 1500 in roughly 44-46 days of logged playtime. |
| `const:hp-ratio-combat` | L60 effective HP ratio — Combat | **3.6** | HP/END | L60 nominal (2.4 dev factor + 0.02x60). L1 measured EXACT 2026-08-25: 121 HP at END 50 = 2.42 = 2.4 + 0.02x1, on a clean naked zero-mastery character - the ratio is level-scaled, see const:hp-ratio-magic note. |
| `const:hp-ratio-stealth` | L60 effective HP ratio — Stealth | **2.8** | HP/END | Validated exact on an L60 character (100 END -> 280 HP). Consistent with the level-scaled model (1.6 dev factor + 0.02x60 = 2.8), unmeasured directly. |
| `const:hp-ratio-magic` | L60 effective HP ratio — Magic | **2.2** | HP/END | L60 nominal value. DECODED 2026-08-25 from two clean naked readings: the HP ratio is level-scaled - ratio(level) = dev spec health factor + 0.02 x level (fact:spec-hp-magicka-factors: Combat 2.4 / Stealth 1.6 / Magic 1.0), giving exactly the KB's L60 values 3.6 / 2.8 / 2.2. Measured: L1 Combat 121 HP at END 50 (2.42 exact); L60 Magic reads 219 at END 100 where the model gives 220 - a consistent off-by-one at L60 (same offset seen in the magicka pool) suggests per-level floor accumulation; treat L60 effective Magic as 2.19-2.20 pending a mid-level reading. |
| `const:hp-spec-mult-combat` | HP specialization multiplier (engine) — Combat | **1.14** | x | Dev-quoted engine script value. Relationship to the effective 3.6/2.8/2.2 ratios: the ratios fold in additional layers (see formula:hp). |
| `const:hp-spec-mult-magic` | HP specialization multiplier (engine) — Magic | **1.033** | x |  |
| `const:hp-spec-mult-stealth` | HP specialization multiplier (engine) — Stealth | **1.077** | x |  |
| `const:magicka-mult-atronach` | Fortify Maximum Magicka — Atronach (Wombburn) | **1.2** | x INT | In-game tooltip reads 1.2x verbatim; the 0.8 dev doc said 1.25x — see contradictions (tooltip adopted as truth). |
| `const:magicka-mult-mage` | Fortify Maximum Magicka — Mage (Fay) | **1.0** | x INT |  |
| `const:magicka-mult-apprentice` | Fortify Maximum Magicka — Apprentice (Elfborn) | **1.5** | x INT |  |
| `const:magicka-mult-altmer` | Fortify Maximum Magicka — High Elf racial | **1.5** | x INT | Validated in-game 2026-08 (exact fit in the flat-stack model). |
| `const:magicka-mult-breton` | Fortify Maximum Magicka — Breton racial | **0.5** | x INT |  |
| `const:int-cap-magicka` | Base INT cap in the magicka formula (un-raised) | **175** | INT | 175 is only the BASE cap: 'Fortification Max' mastery bonuses raise it per character (effective cap = 175 + sum of Intelligence Fortification Max). Magicka scales with INT all the way up to the effective cap (maintainer-stated 2026-08-24); INT above the EFFECTIVE cap adds nothing and corrupts the pool (see fact:overmax-magicka-bug). |
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
| `const:magic-resistance-cap` | Magic resistance cap | **85** | % | Applies to the magic resists (Fire/Frost/Shock/Magicka/Poison and kin). Resist Normal Weapons has its own cap — see const:nw-resist-cap. |
| `const:nw-resist-cap` | Resist Normal Weapons cap | **100** | % | Taken as 100 (maintainer-ruled 2026-08-24, provisional pending a direct player-side reading): the in-game immunity mechanic exists — creatures at Resist Normal Weapons 100 show 'your weapon has no effect' (ghosts) — so full immunity is assumed reachable by players too. Stacks ADDITIVELY like every other resist; only Spell Absorption and Spell Reflect stack multiplicatively. |
| `const:speed-cap` | Speed cap | **— (contested)** |  | 350 (2021 claim) vs 175 at L60 (2024 claim) — see contradictions; unresolved. |
| `const:melding-pct-per-rank` | Melding Construct AR bonus per rank | **4** | %/rank | SETTLED (maintainer-ruled 2026-08-25): the rank-5 endpoint (+20% total equipment AR) is measured — it reconciled a rank-5 owner's armor readings exactly (archive-corroborated exchange, 2026-08-21). The per-rank split (+4% each, increments stack) is the assumed-linear trajectory by analogy with the server's other linear mastery lines; only the split, not the total, rests on that assumption. Applies to equipped-armor AR. |
| `const:anvil-armor-ar-multiplier` | Anvil max upgrade — armor piece AR multiplier | **1.54** | x | PROVISIONAL — one measured item pair (fresh 250 vs maxed 385 at matched skill/condition). A relayed '+42 AR flat' figure did not match — see contradictions. |
| `const:native-magicka-regen` | Native magicka regen | **1** | magicka/tick | For all characters EXCEPT Stunted Magicka (Atronach). Deliberate NP GMST edit. |
| `const:enchant-skill-one-charge` | Enchant skill for 1-charge casts | **110** | skill | At 110 Enchant, all enchanted items cost 1 charge per use (multiple corroborations 2019-2022). |
| `const:max-effects-per-enchant` | Max effects per enchant/spell | **8** | effects | Soul size raises magnitude/duration, never the effect count. |
| `const:vampire-daywalker-cost` | Daywalker perk cost | **50** | mastery points |  |
| `const:vampire-ancient-bloodline-cost` | Ancient Bloodline perk cost | **75** | mastery points | Requires Daywalker first; both together 125 points. |

## Formulas

### Max Health (L60 effective)  
`HP = floor(END x (spec_ratio + sum(health_factor_bonuses))) + flat_fortify_health`  
spec_ratio: see const:hp-ratio-*. Dev-stated structure: HP = Endurance x HP Factor(s) x spec multiplier + flat fortify; every character starts with 1 innate HP Factor; Health-Factor perks add on (+1 HP Factor -> 1 END = 2 HP). Endurance is retroactive/real-time. How +0.2-class Health-Factor mastery lines interact with the L60 ratio is OPEN (q:health-factor-stacking). Independently corroborated 2026-08-23 by the community calculators sheet (HP = END x (specRatio + sum HF) + flat fortify), same structure. HEALTH FACTOR STACKING SETTLED 2026-08-25 from three dated public statements, including a worked example from the community's most authoritative mechanics voice: '.4 hp factor at lv60 with 100end = 40hp ... with 300 end it would be worth 120hp' (2025-03-06, server-general - delta = HF x END, linear in Endurance, i.e. HF adds to the spec ratio); 'health factor improves the endurance to hp ratio' (2026-08-16, in-game); 'increases how much endurance impacts max health', and it is retroactive (2026-08-21, in-game). The additive model this formula encodes is confirmed; a controlled before/after purchase would upgrade to measured but is no longer needed.

### Max Magicka (flat-stack model)  
`maxMagicka = floor( min(INT, INT_cap) x (spec_magicka_factor + 0.025 x level + sum(FortifyMaxMagicka carriers)) )`  
DECODED 2026-08-25 from three clean naked zero-mastery readings - the base is NOT 1 x INT: the dev-stated spec magicka factors (Combat 0.9 / Stealth 1.15 / Magic 1.5, fact:spec-hp-magicka-factors) are live in the pool, plus a 0.025-per-level term (1.5 at L60). Carriers are the displayed 'Fortify Maximum Magicka xINT' effects (signs Atronach 1.2 / Mage 1.0 / Apprentice 1.5; racials Altmer 1.5 / Breton 0.5; items stack the same way). Verification (FOUR clean readings): L1 Combat no-carriers 27 = floor(30 x 0.925) EXACT; L60 Stealth Dunmer/Atronach 385 = 100 x 3.85 EXACT (this reading is the character whose '3.85x slope' was once flagged as a hidden-passive anomaly - the anomaly was the old formula, not the character); L60 Magic Altmer/Atronach 712 = floor(125 x 5.7) EXACT (a vampire - vampirism's documented +20 attribute fortifies are the only effect, INT untouched: the vamp-contamination suspicion is cleared for this character); L60 Magic Breton/Atronach reads 469 where the product is exactly 470.0. Integer-product display map so far: 470.0->469 and (HP) 220.0->219, but 385.0->385 and (HP) 280.0->280 - a value-specific float quirk in the engine, at most 1 low; fractional products floor exactly (27.75->27, 712.5->712). INT_cap = 175 + INT Fortification Max (cap-relative, maintainer-ruled 8/24); behavior above the cap remains untested. The 2026-08-21 'validated' 647 reading is invalidated - no integer INT reproduces it under any candidate model, and that session had documented duplicate-ability instability.

### Max Fatigue  
`maxFat = STR + WIL + AGI + END + level_bonus`  
level_bonus: +55 at L60 (validated exact on two characters), +1 at L1; curve between unmeasured. One L60 Stealth character reads +126 above this model EVEN NAKED WITH ZERO MASTERIES (581 vs 455, re-measured 2026-08-25) - maintainer-ruled 2026-08-25: presumed a character-specific backend bug (forced dev-side mastery respec while werewolf), NOT a mechanic - the formula stands as measured on all clean characters (q:hidden-passive-anomaly resolved; reopen only if a second character shows a surplus). Re-confirmed exact 2026-08-25 on a clean L60 (naked, zero masteries): 100+115+100+100+55=470; a racial Fortify Willpower (+15) counts in the sum. L1 term +1 re-confirmed 2026-08-25 on a clean naked zero-mastery character (181 = 60+30+40+50+1). L60 term +55 re-confirmed 2026-08-25 on a second character (515 = 120+120+120+100+55, vampirism attribute fortifies counting).

### Armor piece tooltip AR  
`tooltipAR = floor(baseAR x armorSkill / 30)`  
Verified for light/medium/heavy at skill 100 and (item-fortified) 118. NP base ARs deviate from vanilla (e.g. Daedric Tower Shield NP base 40 vs vanilla ESM base 80 — see data/vanilla_ref.json) — never take a vanilla base from memory or UESP; vanilla_ref.json is parsed from the game ESMs. [Correction 2026-08-23: an earlier version of this note said 'vanilla 45' — a memory-sourced error caught by the ESM extraction.]

### AR capture-skill normalization convention  
`AR@100 = floor(baseAR x 100/30); baseAR = tooltipReading x 30 / captureSkill`  
CONVENTION: all item AR values in this KB are stated at the skill-100 tooltip baseline (AR@100), independent of who captured them or at what armor skill. Any tooltip captured at a different armor skill MUST be normalized through this formula before entry. Screenshots posted publicly by unknown players may be at unknown skill — such values are marked 'as-posted tooltip, capture skill unknown' in the item record until verified.

### Unarmored slot AR  
`AR_per_slot = unarmoredSkill^2 x 0.0065`  
Skill 100 -> 65; EVERY armor slot not holding an armor item counts at this value x its slot weight - empty slots, clothing-filled slots, AND the empty shield slot (engine-confirmed 2026-08-25: OpenMW getArmorRating gives any slot without an armor item, the shield/carried-left slot included, the unarmored rating (fUnarmoredBase1 x skill) x (fUnarmoredBase2 x skill) = 0.0065 x skill^2; UESP Combat states the same; maintainer-questioned, settled from engine source). Consequence: with high Unarmored, equipping a LOW-AR piece can lower sheet AR, and going shieldless still yields shield-slot AR from Unarmored. The old vanilla-engine bug where Unarmored contributed nothing until at least one armor piece was worn (UESP-documented) is fixed in OpenMW - maintainer-noted 2026-08-25; no such condition exists in the engine code or on NP.

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

### Spell Absorption / Reflect stacking  
`total = 1 - product(1 - eff_i); each added source contributes eff_i x (1 - cumulative_before_it)`  
Multiplicative/diminishing stacking across all sources (gear, potions, sign). Example from the sheet: eighteen sources -> 93% total. APPLIES ONLY to Spell Absorption and Spell Reflect — the only two multiplicative effects in the game; everything else, Sanctuary included, is flat additive (fact:stacking-rules).

### Damage taken vs Armor Rating  
`damageTakenFraction = max(0.25, incomingSwing / (incomingSwing + AR)); damageTaken = incomingSwing x damageTakenFraction`  
Armor mitigation is ratio-based and floors at 25% damage taken (max 75% reduction). Example: AR 1000 vs 2000 swing -> 2/3 damage taken.

### Melee hit chance (attacker)  
`hit% = (WeaponSkill + AGI/5 + LUC/10) x fatigueTerm + AttackBonus - Blind; fatigueTerm ranges 0.75 (empty fatigue) to 1.25 (full)`  
Spec attack penalties per the sheet: Stealth -25, Magic -50. Vanilla-structure formula in community use on NP.

### Evasion (defender)  
`evade% = (AGI/5 + LUC/10) x fatigueTerm + Sanctuary + Dodge; net chance to hit = hit% - evade%`  
Spec dodge penalties per the sheet: Magic -25, Combat -50 (consistent with formula:dodge's spec_penalty). Sanctuary adds 1:1.

### Lockpick / probe success  
`success% = floor((Security + AGI/5 + LUC/10) x toolQuality x fatigueTerm) - lockOrTrapLevel; fatigueTerm 0.75-1.25`  
Tool qualities from the sheet: Grandmaster pick 1.3, Grandmaster probe 1.25.

### Damage taken from mob elemental shields  
`dmg = difficultyMod x 10 x shieldMagnitude x (1 - 0.01 x (playerElementalResist + magicResistRoll)); magicResistRoll = (Destruction + 0.2xWIL + 0.1xLUC) x 1.25 x curFatigue/maxFatigue - RNG(0..99)`  
PROVISIONAL: the sheet's header states TotalResistance = max(100, ...) but its own cells use the raw sum; the x10 multiplier is the sheet's fElementalShieldMult. Explains one-shot deaths at empty fatigue vs giant-class shield mobs (magnitude ~300 -> thousands of damage unresisted).

### Movement speed (walk/run/sneak/swim/fly)  
`walk = (100 + Speed) x (1 - 0.3 x currentEncumbrance/maxEncumbrance); run = walk x (0.01 x Athletics + 1.75); sneak = walk x 0.75; swim = run x (1 + 0.01 x SwiftSwim) x (0.01 x Athletics x 0.1 + 0.5); fly = (5 + 0.01 x (Speed + LevitateMagnitude) x 295) x (1 - 0.3 x currentEncumbrance/maxEncumbrance)`  
PROVISIONAL — the source tab labels itself 'possibly accurate'; engine-GMST structure (fMinWalkSpeed 100, fMaxWalkSpeed 200, fSneakSpeedMultiplier 0.75, fBaseRunMultiplier 1.75, fMinFlySpeed 5, fMaxFlySpeed 300, fEncumberedMoveEffect 0.3, fSwimRunAthleticsMult 0.1, fSwimRunBase 0.5). walk simplifies from fMin + 0.01xSpeed x (fMax-fMin). One in-game timing check would confirm or correct.

### HP ratio level scaling  
`spec_ratio(level) = spec_health_factor + 0.02 x level   (Combat 2.4 / Stealth 1.6 / Magic 1.0 base)`  
Four clean readings: exact at L1 Combat (121 = floor(50 x 2.42)); TWO L60 Magic characters read 219 at END 100 (model 220.0 - value-specific float quirk, see formula:magicka note); L60 Stealth reads 280 = 100 x 2.8 EXACT. L60 values reproduce the established 3.6/2.8/2.2.


## Established facts

- **stacking-rules**: UNIVERSAL STACKING RULE: everything in the game stacks FLAT ADDITIVE — attributes, skills, resists, Sanctuary, Armor Bonus, Attack, Feather, all fortifications — with exactly TWO exceptions: Spell Absorption and Spell Reflect, which stack multiplicatively across sources (total = 1 - product(1 - each); see formula:absorb-reflect-stacking). Sanctuary is NOT Spell Absorption — it is a separate, additive effect and must never be fed into the absorption math.
- **np-not-vanilla**: NP deliberately rewrites vanilla values: birthsigns and racials fully reworked in 0.8, item base stats differ from vanilla/UESP, and core formulas are server-custom. Vanilla knowledge must never be substituted for a missing NP value.
- **restore-vs-tick**: Constant 'Restore Health/Magicka/Fatigue' effects apply per SECOND; 'over Time' (HoT/MoT/FoT) effects apply per 6-second tick.
- **atronach-stunted-regen**: Stunted Magicka (Atronach) removes the native 1 magicka/tick regen AND halves all mastery-gained HoT/MoT/FoT tick regen; item-granted regen is not halved.
- **atronach-drain** **[provisional]**: As part of the 0.8 Atronach rework, the sign carries a self Damage Magicka effect (5% of total maximum magicka) — dev-described as a slow drain 'unless you do something about it'. Whether the drain is still live in the current era is unconfirmed.
- **overmax-system**: Overmaxing is a general server system covering attributes AND skills: each stat's allowed maximum = its base cap + that stat's 'Fortification Max' mastery bonuses, and a stat pushed above that cap is 'overmaxed'. The server detects and handles overmaxed stats — historically via a visible drain effect, removed from the effects list in the 1/16/2026 update; /inspect displays overmaxed values since that update. Overmax behavior in werewolf form is dev-acknowledged as still quirky. Effects that scale off a stat (e.g. Focused Strike's Agility-scaled proc chance) read the CAPPED effective value, never the raw overmaxed value - that is the point of caps (maintainer-ruled 2026-08-25). Raw points above the cap are wasted for scaling purposes as well as being overmax-unstable.
- **overmax-magicka-bug**: Raising INT above your EFFECTIVE cap (175 base + Intelligence Fortification Max mastery bonuses) does not just waste points — it CORRUPTS max magicka, and the corrupted value re-rolls on every relog (swinging high or low). INT above 175 is SAFE as long as it sits under your raised cap; overmax only applies when the cap is below the stat (an INT-181 character with a 260 cap was previously mislabeled overmaxed — maintainer-corrected 2026-08-24). Dev-acknowledged as an open issue (Jan 2026) and community-confirmed (Aug 2026). Fixes: damage INT, unequip INT gear to get under your cap, or relog.
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
- **respec-paths**: Two DIFFERENT mechanisms (maintainer-verified in-game 2026-08-25, dialogue screenshot): (1) MASTERY POINT refunds go through Rehabilitator Anja (Vivec, near the bank) - the paid path, community-reported around 450k gold. (2) Socucius Ergalla's one-time free level-60 respec changes the CHARACTER BUILD - his dialogue offers to update the 'Release Identification' (birthsign, class, or race) 'just this once' - it does NOT refund mastery points. The old note treating these as possibly one mechanism is superseded; the earlier 'zero CM points currently spent' condition and the anniversary extra-respec report attach to the Socucius character respec as previously recorded, not to Anja refunds.
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
- **potion-active-limit-values**: Active-potion limit, dev-stated curve (2019-07-05 announcement): Alchemy <50 = 3, 50-74 = 4, 75-99 = 5, 100+ = 6. Current-era player reports (2025-2026) consistently say 5 at Alchemy 100 with the Cowl of the Druid raising it to 6 — see c:active-potion-limit; the curve may have been retuned since 2019.
- **potions-per-combine**: A fully equipped player alchemist gets 5 potions per combine.
- **potion-effect-caps**: Player-made potion magnitudes and durations are capped server-side: a maximum brewable value per effect exists ('maxed potions'). Elemental shield, resist, and fatigue effects escaped the across-the-board potion cap pass. Potions brewed before the cap pass ('pre-nerf' batches) persist in circulation and can exceed current brew ceilings.
- **potion-strength-inputs**: Potion strength scales with Alchemy skill first, then Intelligence, then Luck; skipping any max-investment source (racial line, Godborn) docks roughly 1 point of potion strength each. Current-era max-potion meta: Breton or Altmer, maxed Alchemy/INT/Luck, Metabolist master class, full Secret Master apparatus set.
- **ingredient-eating-first-effect**: Eating an ingredient raw grants only its first-listed effect.
- **vampire-dust-vampirism-cosmetic**: The Vampirism effect on Vampire Dust changes the drinker's appearance only; it carries none of the actual vampirism scripting.
- **mass-brew-caution**: Very large single combines are risky: a 1000-potion combine triggered the server's anti-cheat auto-ban, and mass brewing lags the server. Community practice is roughly 100 potions per combine with a few seconds between batches.
- **alchemist-cm-budget**: A max-potency alchemist build was publicly accounted at ~950 CM: ~500 in base lines (Curiosity, max INT/Luck/Alchemy plus filler), 200 Metabolist master class, 75+75 for its two master-class abilities, and 100 Godborn.
- **xp-kill-bonus-stacking**: Kill-XP bonuses combine as: factor = 1 + max(Luck event 1.0, basic XP potion 0.5, Jiubmas Cheer 1.5) + 0.1 per XP-clothing piece + 1.0 during Happy Hour. Luck event / XP potion / Cheer do NOT stack with each other (best one applies); clothing and Happy Hour stack on top.
- **party-xp-split**: Group XP split multipliers (measured at dreugh during Happy Hour): 1 player 1.000, 2 players 0.9615, 3 players 0.9259, 4 players 0.8929 of solo per-kill XP each — a full group loses ~11% per head but yields ~3.57x total group XP.
- **ww-potion-buffing**: Werewolf play is potion-driven: buffs consumed in human form persist into beast form, so the standard loop is buff (potions and spells) in human form, then swap. WW builds are advised to reach Alchemy 100 for the 5-active-potion limit, with the Cowl of the Druid (+1, to 6) as recommended human-form gear.
- **ww-gear-no-transfer**: Equipment stats do NOT carry into werewolf form — human-form gear is preference only — with one exception: the Endowment System robe/skirt (quest west of the Gnisis silt strider), whose effects become permanent on the character and persist through the swap.
- **spec-hp-magicka-factors**: Dev-stated specialization factors (2023-10-22 announcement): Health — Combat 2.4, Stealth 1.6, Magic 1.0; Magicka — Combat 0.9, Stealth 1.15, Magic 1.5.
- **quickkey-potion-ban**: Potions and scrolls cannot be bound to Quick Keys (dev-stated, introduced with the active-potion limit).
- **potion-limit-clears-on-death**: Active potion limitations clear on death (dev-stated fix, closing a bypass exploit).
- **invis-crit-limiter**: A custom server mechanic limits players' ability to spam invisibility-based critical hits. A player who noticed invisibility felt less reliable was told this reduction is intentional (dev-stated, 2022-11-01).
- **sujamma-vs-player-potions**: Dev-stated (2022-11-30, settling a public debate): alchemy-mastery-invested player potions are far superior to Sujamma on overall effects. Sujamma boosts Strength 50 but subtracts Intelligence 50, canceling its net attribute value; the debate's example mastery-invested player potion granted +98 total attribute points, +140 Fortify Health, and +61 disease resist, each effect lasting 10 seconds longer than Sujamma's, with zero negative effects. Sujamma remains the cheap convenience only when a single stat alone matters and alchemy masteries are uninvested.
- **vampirism-passives**: Vampirism grants constant passives: +20 Agility/Strength/Willpower/Speed; +30 to eight skills (Unarmored, Sneak, Hand-to-Hand, Athletics, Destruction, Illusion, Mysticism, Acrobatics); Resist Paralysis 100; Disease immunity 100; Resist Normal Weapons +50; Weakness to Fire 50. Clan bonuses stack on top (fact:vampire-clan-bonuses).
- **vampire-clan-bonuses**: Each vampire clan adds +20 to one attribute and three skills, on top of the base vampirism passives: Aundae — +20 Willpower and +20 Short Blade/Mysticism/Destruction; Berne — +20 Agility and +20 Sneak/Unarmored/Hand-to-Hand; Quarra — +20 Strength and +20 Blunt Weapon/Hand-to-Hand/Heavy Armor.
- **enhancement-effect**: The server-custom 'Enhancement N pts' constant effect on items (jewelry/clothing: Murk Claw Ring, Martial Band, Belt of Fish Scales, Glowing Heroic Band, Rune Etched Choker, Frost Etched Belt) adds N flat Armor Rating while equipped. The character sheet refreshes the value only after reopening the inventory. Corroborated three times independently (2025-12-21 owner reading; 2026-08-03; 2026-08-14). Note: one report links swapping Enhancement gear to armor-skill display fluctuation, suggesting an armor-skill-fortification implementation under the hood; the flat-AR outcome is the player-verified behavior.
- **native-hp-regen**: Characters natively regenerate 5% of max health every 6-second tick ('you regen 5% of your max every 6sec', 2026-08-16, in-game chat; corroborated in-thread: 'Max hp also impacts regen'). As-stated by a veteran player; conditions (combat state, vampirism/Atronach interactions) unmeasured.
