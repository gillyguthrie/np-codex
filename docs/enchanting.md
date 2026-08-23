<!-- GENERATED from data/enchanting.json by tools/generate_docs.py — do not hand-edit. -->

# NP Enchanting & Infusion Anvil

NP enchanting and Infusion Anvil system. The self-enchant baseline chart is EMPIRICAL — observed maxima on real player-enchanted items — not a dev-published table. Era matters: the anvil was reworked twice; only post-Jan-2026 values are current.


## Self-enchant baseline (observed maxima)

Max observed constant-effect magnitude per blank slot x effect class. 'Fortify class' = fortify attribute/skill/attack; Chameleon and Sanctuary price identically to fortify. Armor slots (except helm and shield) hold far less than clothing — cuirass/pauldrons/greaves/boots/gauntlets are not practical self-enchant targets.

| slot | fortify | restore HP | levitate/jump | other |
|---|---|---|---|---|
| ring (grand/exquisite) | 55 | 10 | 17 | Chameleon/Sanctuary observed 56 |
| amulet (grand) | 55 | 10 | 17 |  |
| helm (armor blank) | 59 | 11 |  |  |
| shield (daedric-tower-class) | 88 | 17 |  | Sanctuary/Chameleon observed 87-89 |
| shirt/pants/skirt (grand) | 29 | 5 |  |  |
| robe (grand) | 30 |  |  |  |
| shoes (grand) | 19 | 3 | 5 | resist elemental 9 |
| gloves (grand) | 11 |  |  | resist paralysis 50 |
| belt (grand) | ? |  |  | no enchanted example observed; inferred ~29 (shirt-class), unverified |

**EV cost ratios** (fortify=1.0x, ~±20%): fortify 1.0x, sanctuary_chameleon 1.0x, resist_elemental 2.1x, levitate_jump 3.5x, restore_health 5.6x, resist_paralysis 0.2x

## Facts

- EV (Enchant Value) is how strong an enchantment an item can hold; every weapon, apparel item, and blank scroll has one.
- Post-0.8 constant-effect enchants roll between min and max (enchanter mastery/racials improve odds); later reports say outcomes auto-set to the range average. Always enter ranges as 1-X, never X-X.
- Max 8 effects per enchant/spell regardless of soul size; bigger souls raise magnitude/duration only.
- At Enchant skill 110, all enchanted items cost 1 charge per use (multiple corroborations 2019-2022); at 109 some still cost more.
- The reliable self-enchant ceiling is items of ~100 EV or below (expert community testing).
- Exquisite/grand ring baseline is ~20-24 EV; a re-equip-during-enchant technique historically reached 47 points on a ring (may since be patched — verify before relying on it). **[provisional]**
- Disenchanting (mastery) extracts a player enchant with an empty black soul gem, which shatters; the item returns to its blank state and can be re-enchanted.
- Player enchants have no NPC-sale gold value.
- Self-enchanted fortify effects do not persist across login — a re-equip shuffle after logging in reapplies them.
- Weapon enchants are cast-on-strike/charge-based — a different system from constant-effect apparel enchants. Damage-on-strike enchants are not mitigated by the target's Armor Rating.
- Glamouring a weapon can inconsistently break its silver flag or damage-type flag (e.g. a Daedric weapon glamoured with a Steel model losing its ability to damage Daedra); reproduction attempts have failed on other models — model-specific or intermittent. **[provisional]**
- Charges consumed per cast/strike = ROUNDUP(effect total EV x (1.1 - EnchantSkill/100)), minimum 1; uses until empty = floor(soulCharge / chargesPerCast). Example: 140 EV at Enchant 108 -> ceil(140 x 0.02) = 3 charges/cast; a 1500 soul gives 500 uses.

## Infusion Anvil (2026-08)

Infusion Anvil item upgrading. 6 attempts per item; outcomes fail / success / critical. History: Nov 2025 first version too strong -> upgraded items wiped; Jan 2026 rebalance; Aug 2026 community confirmation that 'upgrade values are fixed'. Only current-era numbers below.

- **jewellery and clothing**: +55 EV — displays as 5x9 + 1x10 on rings; non-critical roughly half
- **weapons**: +30 Damage, +2250 Durability, +25 EV
- **armor**: +25 EV, +2250 Durability; AR gain CONTESTED — a relayed '+42 AR' estimate vs a measured x1.54 piece-AR pair (see mechanics const:anvil-armor-ar-multiplier and contradictions)
- Luck has little to no measurable influence on upgrade outcomes; tradeskill levels do not influence upgrade costs or salvage yield.
- Enchant skill primarily influences EV gains (rings/clothing); Armorer skill primarily influences AR/damage/durability gains (weapons/armor).
- Upgrades use fixed increments per item type, not percentages — item quality/material is irrelevant to the increment (e.g. fully upgraded common gloves can exceed fully upgraded Daedric gloves in EV).
- Upgrading does NOT change existing enchantments — upgrade the blank first, then enchant. Whether enchant magnitude ceilings scale with upgraded EV is OPEN (one test enchant settles it).
