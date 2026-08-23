#!/usr/bin/env python3
"""Parse vanilla equipment (ARMO/WEAP/CLOT + ENCH) from local Morrowind ESMs
into data/vanilla_ref.json. Later ESMs override earlier (load order).
Usage (from repo root): python tools/build_vanilla_ref.py "<path to Morrowind Data Files>"
Rewrites data/vanilla_ref.json and refreshes items.json xref["vanilla-ref"] links."""
import struct, json, re, unicodedata
from pathlib import Path

import sys
ESM_DIR = Path(sys.argv[1] if len(sys.argv)>1 else "C:/Games/Morrowind/Morrowind/Data Files")
LOAD_ORDER = ["Morrowind.esm", "Tribunal.esm", "Bloodmoon.esm"]

EFFECTS = {0:"Water Breathing",1:"Swift Swim",2:"Water Walking",3:"Shield",4:"Fire Shield",5:"Lightning Shield",6:"Frost Shield",7:"Burden",8:"Feather",9:"Jump",10:"Levitate",11:"SlowFall",12:"Lock",13:"Open",14:"Fire Damage",15:"Shock Damage",16:"Frost Damage",17:"Drain Attribute",18:"Drain Health",19:"Drain Magicka",20:"Drain Fatigue",21:"Drain Skill",22:"Damage Attribute",23:"Damage Health",24:"Damage Magicka",25:"Damage Fatigue",26:"Damage Skill",27:"Poison",28:"Weakness to Fire",29:"Weakness to Frost",30:"Weakness to Shock",31:"Weakness to Magicka",32:"Weakness to Common Disease",33:"Weakness to Blight Disease",34:"Weakness to Corprus",35:"Weakness to Poison",36:"Weakness to Normal Weapons",37:"Disintegrate Weapon",38:"Disintegrate Armor",39:"Invisibility",40:"Chameleon",41:"Light",42:"Sanctuary",43:"Night Eye",44:"Charm",45:"Paralyze",46:"Silence",47:"Blind",48:"Sound",49:"Calm Humanoid",50:"Calm Creature",51:"Frenzy Humanoid",52:"Frenzy Creature",53:"Demoralize Humanoid",54:"Demoralize Creature",55:"Rally Humanoid",56:"Rally Creature",57:"Dispel",58:"Soultrap",59:"Telekinesis",60:"Mark",61:"Recall",62:"Divine Intervention",63:"Almsivi Intervention",64:"Detect Animal",65:"Detect Enchantment",66:"Detect Key",67:"Spell Absorption",68:"Reflect",69:"Cure Common Disease",70:"Cure Blight Disease",71:"Cure Corprus Disease",72:"Cure Poison",73:"Cure Paralyzation",74:"Restore Attribute",75:"Restore Health",76:"Restore Magicka",77:"Restore Fatigue",78:"Restore Skill",79:"Fortify Attribute",80:"Fortify Health",81:"Fortify Magicka",82:"Fortify Fatigue",83:"Fortify Skill",84:"Fortify Maximum Magicka",85:"Absorb Attribute",86:"Absorb Health",87:"Absorb Magicka",88:"Absorb Fatigue",89:"Absorb Skill",90:"Resist Fire",91:"Resist Frost",92:"Resist Shock",93:"Resist Magicka",94:"Resist Common Disease",95:"Resist Blight Disease",96:"Resist Corprus Disease",97:"Resist Poison",98:"Resist Normal Weapons",99:"Resist Paralysis",100:"Remove Curse",101:"Turn Undead",102:"Summon Scamp",103:"Summon Clannfear",104:"Summon Daedroth",105:"Summon Dremora",106:"Summon Ancestral Ghost",107:"Summon Skeletal Minion",108:"Summon Bonewalker",109:"Summon Greater Bonewalker",110:"Summon Bonelord",111:"Summon Winged Twilight",112:"Summon Hunger",113:"Summon Golden Saint",114:"Summon Flame Atronach",115:"Summon Frost Atronach",116:"Summon Storm Atronach",117:"Fortify Attack",118:"Command Creature",119:"Command Humanoid",120:"Bound Dagger",121:"Bound Longsword",122:"Bound Mace",123:"Bound Battle Axe",124:"Bound Spear",125:"Bound Longbow",126:"EXTRA SPELL",127:"Bound Cuirass",128:"Bound Helm",129:"Bound Boots",130:"Bound Shield",131:"Bound Gloves",132:"Corprus",133:"Vampirism",134:"Summon Centurion Sphere",135:"Sun Damage",136:"Stunted Magicka",137:"Summon Fabricant",138:"Call Wolf",139:"Call Bear",140:"Summon Bonewolf",141:"sEffectSummonCreature04",142:"sEffectSummonCreature05"}
ATTRS = ["Strength","Intelligence","Willpower","Agility","Speed","Endurance","Personality","Luck"]
SKILLS = ["Block","Armorer","Medium Armor","Heavy Armor","Blunt Weapon","Long Blade","Axe","Spear","Athletics","Enchant","Destruction","Alteration","Illusion","Conjuration","Mysticism","Restoration","Alchemy","Unarmored","Security","Sneak","Acrobatics","Light Armor","Short Blade","Marksman","Mercantile","Speechcraft","Hand-to-hand"]
RANGES = {0:"Self",1:"Touch",2:"Target"}
ENCH_TYPES = {0:"cast-once",1:"cast-on-strike",2:"cast-when-used",3:"constant"}
ARMOR_TYPES = {0:"Helmet",1:"Cuirass",2:"Left Pauldron",3:"Right Pauldron",4:"Greaves",5:"Boots",6:"Left Gauntlet",7:"Right Gauntlet",8:"Shield",9:"Left Bracer",10:"Right Bracer"}
CLOT_TYPES = {0:"Pants",1:"Shoes",2:"Shirt",3:"Belt",4:"Robe",5:"Right Glove",6:"Left Glove",7:"Skirt",8:"Ring",9:"Amulet"}
WEAP_TYPES = {0:"Short Blade 1H",1:"Long Blade 1H",2:"Long Blade 2H",3:"Blunt 1H",4:"Blunt 2H Close",5:"Blunt 2H Wide",6:"Spear 2H",7:"Axe 1H",8:"Axe 2H",9:"Marksman Bow",10:"Marksman Crossbow",11:"Marksman Thrown",12:"Arrow",13:"Bolt"}

def subrecords(data):
    o=0
    while o+8<=len(data):
        name=data[o:o+4].decode('ascii',errors='replace'); size=struct.unpack('<I',data[o+4:o+8])[0]
        yield name,data[o+8:o+8+size]; o+=8+size

def records(path):
    b=path.read_bytes(); o=0
    while o+16<=len(b):
        name=b[o:o+4].decode('ascii',errors='replace'); size=struct.unpack('<I',b[o+4:o+8])[0]
        yield name,b[o+16:o+16+size]; o+=16+size

def zstr(x): return x.split(b'\x00')[0].decode('cp1252',errors='replace')

def parse_effects(blobs):
    out=[]
    for e in blobs:
        eff,skill,attr,rng,area,dur,mn,mx=struct.unpack('<hbbiiiii',e[:24])
        nm=EFFECTS.get(eff,f"effect#{eff}")
        if nm in("Fortify Attribute","Drain Attribute","Damage Attribute","Absorb Attribute","Restore Attribute"):
            nm=f"{nm.split()[0]} {ATTRS[attr] if 0<=attr<8 else attr}"
        elif nm in("Fortify Skill","Drain Skill","Damage Skill","Absorb Skill","Restore Skill"):
            nm=f"{nm.split()[0]} {SKILLS[skill] if 0<=skill<27 else skill} (skill)"
        out.append({"effect":nm,"range":RANGES.get(rng,rng),"area":area,"duration":dur,"mag_min":mn,"mag_max":mx})
    return out

ench={}; items={}
for esm in LOAD_ORDER:
    for rname,body in records(ESM_DIR/esm):
        if rname=='ENCH':
            rid=None; edata=None; effs=[]
            for sn,sd in subrecords(body):
                if sn=='NAME': rid=zstr(sd)
                elif sn=='ENDT': edata=struct.unpack('<iiii',sd[:16])
                elif sn=='ENAM': effs.append(sd)
            if rid and edata:
                ench[rid.lower()]={"type":ENCH_TYPES.get(edata[0],edata[0]),"cost":edata[1],"charge":edata[2],"autocalc":bool(edata[3]),"effects":parse_effects(effs)}
        elif rname in('ARMO','WEAP','CLOT'):
            rid=None;fname=None;edict={};script=None;dat=None
            for sn,sd in subrecords(body):
                if sn=='NAME': rid=zstr(sd)
                elif sn=='FNAM': fname=zstr(sd)
                elif sn=='ENAM': edict['ench_id']=zstr(sd)
                elif sn=='SCRI': script=zstr(sd)
                elif sn in('AODT','WPDT','CTDT'): dat=(sn,sd)
            if not rid or not fname or not dat: continue
            kind,sd=dat; rec={"esm_id":rid,"name":fname,"src_esm":esm}
            if script: rec["script"]=script
            if kind=='AODT':
                t,w,v,h,e,ar=struct.unpack('<ifiiii',sd[:24])
                rec.update(kind="armor",subtype=ARMOR_TYPES.get(t,t),weight=round(w,2),value_gold=v,health=h,enchant_capacity=e/10,ar_base=ar)
            elif kind=='CTDT':
                t,w,v,e=struct.unpack('<ifHH',sd[:12])
                rec.update(kind="clothing",subtype=CLOT_TYPES.get(t,t),weight=round(w,2),value_gold=v,enchant_capacity=e/10)
            elif kind=='WPDT':
                w,v,t,h,sp,reach,e,c1,c2,s1,s2,t1,t2,fl=struct.unpack('<fiHHffHBBBBBBi',sd[:32])
                rec.update(kind="weapon",subtype=WEAP_TYPES.get(t,t),weight=round(w,2),value_gold=v,health=h,
                           speed=round(sp,2),reach=round(reach,2),enchant_capacity=e/10,
                           dmg={"Chop":[c1,c2],"Slash":[s1,s2],"Thrust":[t1,t2]},
                           flags={"ignores_normal_weapon_resistance":bool(fl&1),"silver":bool(fl&2)})
            rec.update(edict)
            items[rid.lower()]=rec  # later ESM overrides

for r in items.values():
    eid=r.pop('ench_id',None)
    if eid:
        r["enchantment"]=ench.get(eid.lower(),{"note":f"enchant record '{eid}' not found"})

def slug(name):
    s=unicodedata.normalize('NFKD',name).encode('ascii','ignore').decode()
    s=re.sub(r"[^a-z0-9]+","-",s.lower()).strip('-')
    return s

out=[]; seen=set()
for r in sorted(items.values(),key=lambda x:(x['name'].lower(),x['esm_id'].lower())):
    base="vanilla:"+slug(r['name']); sid=base
    if base in seen:
        sid=base+"--"+slug(r['esm_id'])
    seen.add(base); seen.add(sid)
    out.append({"id":sid,**r})

np=json.load(open('data/items.json'))
by_name={}
for r in out: by_name.setdefault(r['name'].lower(),[]).append(r['id'])
nmatch=0
for it in np['items']:
    if it.get('origin_game')=='vanilla':
        hits=by_name.get(it['name'].lower())
        if hits:
            it.setdefault('xref',{})['vanilla-ref']=hits[0]; nmatch+=1
json.dump(np,open('data/items.json','w'),indent=1,ensure_ascii=False)
open('data/items.json','a').write('\n')

doc={
 "_meta":{
  "description":"Vanilla Morrowind equipment reference (armor, weapons, clothing incl. rings/amulets) parsed directly from the game's ESM files (Morrowind + Tribunal + Bloodmoon, later files override earlier). Purpose: ground NP-vs-vanilla item comparisons and answer vanilla stat lookups without memory or wiki dependence. This file describes VANILLA values only — never valid NP values.",
  "extraction_date":"2026-08-23",
  "conventions":{
   "ar_base":"The raw ESM armor rating — the tooltip value at armor skill 30. Player tooltip at skill S = floor(ar_base x S/30); at skill 100 = floor(ar_base x 10/3). NP's items.json stores AR at the skill-100 convention, so to compare: vanillaAR@100 = floor(ar_base x 100/30).",
   "enchant_capacity":"Displayed (CS/tooltip) enchant points; the ESM stores this x10 and it is divided back here.",
   "speed":"Weapon swing-speed multiplier (1.0 = baseline). NP tooltips express this as a percentage (e.g. 2.5 -> 250%).",
   "dmg":"[min,max] per swing type. Constant-effect enchantments have type 'constant'; per-effect duration values on constant enchants are engine artifacts and not meaningful.",
   "ids":"id is a slug of the display name; display-name collisions get an --esm-id suffix. esm_id is the authoritative game object id."
  },
  "counts":{"records":len(out),"enchanted":sum(1 for r in out if 'enchantment' in r),"np_xref_matches":nmatch}
 },
 "sources":{"s-esm":{"origin":"game-esm","channel":None,"url":None,"date":"2026-08-23","confidence":"dev-stated","note":"Parsed from local Morrowind.esm / Tribunal.esm / Bloodmoon.esm — the shipped game data itself."}},
 "items":out
}
json.dump(doc,open('data/vanilla_ref.json','w'),indent=1,ensure_ascii=False)
open('data/vanilla_ref.json','a').write('\n')
print("records:",len(out),"enchanted:",doc['_meta']['counts']['enchanted'],"np_xref:",nmatch)
for want in ("daedric tower shield","keening","sunder","exquisite ring"):
    for r in out:
        if r['name'].lower()==want:
            keep={k:v for k,v in r.items() if k in('ar_base','weight','value_gold','health','enchant_capacity','speed','dmg','subtype','kind')}
            print(want.upper(),":",json.dumps(keep))
            break
