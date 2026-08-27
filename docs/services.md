<!-- GENERATED from data/services.json by tools/generate_docs.py — do not hand-edit. -->

# NP Player Services

NP player services and world systems: purchasable housing, the Login Points currency and its exchange, and the appearance systems (Dwemer Glamour Analyzer, passive robe/skirt endowment). Captured from in-game dialog and menus, plus the Fishing tradeskill system (Fishing Guru, bait, Fishing Points, crates, fishing bosses).


## Player Housing

**Service NPC:** Bim Joonie — Just north of the Bank of Vivec (warp gate beside him); offers a full explanation and viewable display models

- Homes are purchased for a flat fee dependent on home size and included amenities.
- Travel to a purchased home by interacting with a warp gate (one stands next to the housing vendor).
- Purchased homes have an upkeep cost paid BIWEEKLY; it can be paid up to one week in advance.
- Failing to pay upkeep never forfeits the home or anything inside it — you simply cannot enter again until the upkeep cost is paid.
- Unpaid upkeep does not stack: you never owe more than the one flat upkeep cost, regardless of how long it takes to pay.

| Home | Price |
|---|---|
| Stoneflower Cottage | 1,250,000 gold (1.250m gold) |
| Weaver's Cistern | 1,250,000 gold (1.250m gold) |
| Rose Hilt Hall | 1,250,000 gold (1.250m gold) |
| Hlaalu Tower | 350,000 gold (350k gold) |
| Hlaalu Outfitter | 350,000 gold (350k gold) |
| Hlaalo Manor | 1,000,000 gold (1m gold) |
| Nerano Manor | 1,000,000 gold (1m gold) |
| Tyravel Manor | 1,000,000 gold (1m gold) |
| Hlaalu Council Manor | 2,000,000 gold (2m gold) |

*Upkeep amounts per home were not captured. House building/customization exists beyond purchase but is uncaptured — see open_questions.*

## Login Points

**Service NPC:** Duharr — Docks of Suran (Khajiit trader with a pack guar) — 'This one trades goods to those who visit Vvardenfell often.'

- Each normal login grants 18 Login Points.
- Login points may be boosted during events. *[provisional]*

### Imported Goods

| Item | Cost (Login Points) |
|---|---|
| [Loot Cache]: Jiub Care Package | 140 |
| [Loot Cache]: Jiubsmas Imports | 90 |
| [Loot Cache]: Morroween Imports | 70 |
| [Loot Cache]: Skyrim Imports | 70 |

### Potions

| Item | Cost (Login Points) |
|---|---|
| Alchemie's Secret Brew | 70 |
| Flin | 30 |
| Greef | 60 |
| Mazte | 30 |
| Shein | 30 |
| Skooma | 70 |
| Sujamma | 60 |

### Tradeskill Resources

| Item | Cost (Login Points) |
|---|---|
| Black Lichen | 70 |
| Kresh Fibers | 70 |
| Scrap Metal | 70 |
| Raw Iron | 70 |

### Soul Gems

| Item | Cost (Login Points) |
|---|---|
| Grand Soul Gem | 200 |
| Greater Soul Gem | 160 |
| Common Soul Gem | 120 |
| Lesser Soul Gem | 80 |
| Petty Soul Gem | 40 |

### Miscellaneous Items

| Item | Cost (Login Points) |
|---|---|
| Black Soul Gem | 150 |
| Rose of Renewal | 600 |
| Odd Dwemer Device | 400 |

### Mannequins

20 mannequins: male and female of all ten playable races (Altmer, Argonian, Bosmer, Breton, Dunmer, Imperial, Khajiit, Nord, Orsimer, Redguard), every one at 40 points.

| Item | Cost (Login Points) |
|---|---|
| Mannequin: <race> <sex> | 40 |

*Category counts as shown in the menu: Imported Goods (4), Potions (7), Tradeskill Resources (4), Soul Gems (5), Miscellaneous Items (3), Mannequins (20).*

## Dwemer Glamour Analyzer

**Location:** — (unknown) The machine stands where Enchantress Tessarina lives (coastal site in the captures); cell name not captured.

- Alters the appearance of equipment — applies a different appearance to most weapons, clothing, and armor.
- Glamour Storage holds items used as base glamours; their visual appearance can be applied onto other items of the same type. Stored items can be freely removed whenever desired.
- Maximum Storage Capacity: 10. Capacity can be increased when certain prerequisites are met.
- The Transmogrification Chamber is where an item is prepared to have a glamour applied or removed. Items must be of similar type to successfully apply glamours.
- Glamoured items become UNTRADEABLE until the applied glamour is cleared.
- Non-enchanted glamoured items cannot be enchanted until the applied glamour is cleared.
- Some items are too complex and either cannot be used as a base glamour or cannot have a glamour applied to them.

*Menu: Explanation / Glamour Storage / Transmogrification Chamber.*

## Passive Robe/Skirt Endowment

**Service NPC:** Enchantress Tessarina — Beside the Dwemer Glamour Analyzer (coastal site in the captures; cell name not captured)

- Endows you with a passive Robe or Skirt enchantment: hand over a Constant Effect enchanted robe or skirt, and as long as you are not wearing an item of that type, you are endowed with the Constant Effects of the item she holds.
- The handed-over item leaves your inventory and is kept safe by her until you retrieve it or switch the endowment to another item.
- 10,000 gold per service. The gold is taken immediately when 'Set Passive Enchants' is clicked — no warning or confirmation dialog first.
- She asks for the Ravenback Robe as a prerequisite before offering her services ('Think of the robe as a prerequisite to me offering my services').
- Lets you carry robe/skirt constant effects without the appearance — e.g. benefits of a robe without it covering your armor.

## Fishing

**Service NPC:** Fishing Guru — Khuul (fishing rods can also be found/stolen from houses in Khuul)

- Fishing launched on the current server 2025-06-02 ('Adventurers are now able to fish! Seek out the Fishing Guru in Khuul'). There are over 2,000 unique fish with various weights and ingredient effects; fish are server-generated ingredient items (dev-stated 2026-01-02), so a fishing-caught 'Small Slaughterfish' is a distinct item from the creature corpse's loot.
- Equip a fishing rod, attach bait via the /bait menu, aim the bobber at a body of water, then activate sneak mode to cast the line (in-game tutorial text, log-captured). The /fish command gives fishing info and functionality. Reeling a catch takes ~26s on average (measured range 10-382s).
- Exteriors only (dev-stated 2025-06-02). Players report no fishing in Mournhold, dungeons, or lava; whether player-home fishing is blocked or was only bugged at launch is unresolved (see q:player-home-fishing).
- Crafted bait always beats raw ingredients: 'anything with bait in its name is going to be significantly better than their required ingredients' (dev-stated 2025-07-14). Tiers run from lower/average/beginner up through expert to Master Bait. Bait is consumed; a fish escapes with the bait on roughly 10% of catches (measured). Starter bait: crab meat from the mudcrab camp; ogrims drop master-bait ingredients. Meteor Slime doubles as average-tier bait but is a leftover from a scrapped bait plan and is explicitly bad for boss-spawning (dev-stated 2025-07-15).
- Measured over ~2,200 catches (2025-06): average 520-552 fishing XP per catch, range 12-3,441; XP scales with fish weight (~60 XP/lb rough fit). Crafting above your tradeskill level gives bonus XP; fishing XP counts as tradeskill XP for guild perks (dev-stated). Level 10 is community-estimated at 750+ hours; leveling unlocks better bait and Guru stock.
- When fish stop biting, moving a short distance away resumes fishing and grants a decaying fish-XP boost scaled by distance moved, up to +35% (update notes 2025-07-22). The earlier change-cells requirement (2025-06-10) and the periodic-movement requirement were both later removed (update notes, early 2026: an AFK-kick fix replaced the anti-AFK fishing script).
- The Fishing Guru exchanges caught fish for Fishing Points (update notes 2025-06-04), spendable on bait, 30-minute fishing-benefit potions (fishing XP, crate boosting), recipes, and novelty items. Higher fishing level unlocks more of the Guru's stock.
- Fishing also catches regional crates whose loot tables are region-specific (players catalog Frost Crates on Solstheim, Ashwood Crates in the Ashlands, Stonehewn Crates, Costal Drift Crates on Azura's Coast, Ascadian Wine Crates), plus jars and message-in-a-bottle notes. Reported crate uniques include the Captain's Leg, Cotidal Hammer, Frozenmourn, the Bog Rune armor pieces, Fishbone Tunic, and stalhrim fishing longswords. An orange-text catch with a howl sound is the rarest tier (player-reported 2025-06-05).
- Fishing Buckets store caught fish in several sizes (small ~500, medium ~2,000 per player reports); all fish containers had capacity quadrupled 2025-08-12. Only the largest bucket has a deposit-all button (dev-stated 2026-07-25).
- Fishing Permits obtainable through fishing raise a player home's item cap by 50 items each, once per permit per home; with the biggest houses the practical cap reported is 2,000 items (player-reported 2026).
- Two bosses (Lil Snappa and the Dreughnaught) are spawnable through certain conditions while fishing; activating their corpse distributes loot to all online participants (update notes 2025-06-02), tightened 2025-08-12 to require active participation. See camp:fishing-boss-spawns for the boss records.

*Compiled 2026-08-27 from server-updates patch notes (2021-2026), server-general and in-game-chat archives, and two OCR'd fishing session logs (2025-06-15/16).*
