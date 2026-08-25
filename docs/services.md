<!-- GENERATED from data/services.json by tools/generate_docs.py — do not hand-edit. -->

# NP Player Services

NP player services and world systems: purchasable housing, the Login Points currency and its exchange, and the appearance systems (Dwemer Glamour Analyzer, passive robe/skirt endowment). Captured from in-game dialog and menus.


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
