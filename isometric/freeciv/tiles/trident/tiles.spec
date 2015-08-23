
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
    Tatu Rissanen <tatu.rissanen@hut.fi>
    Jeff Mallatt <jjm@codewell.com> (miscellaneous)
    Eleazar (buoy)
    Vincent Croisier <vincent.croisier@advalvas.be> (ruins)
    Michael Johnson <justaguest> (nuke explosion)
    The Square Cow (inaccessible terrain)
"

[file]
gfx = "trident/tiles"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 30
dy = 30

tiles = { "row", "column", "tag"

; Grassland, and whether terrain to north, south, east, west 
; is more grassland:

  1,  0, "t.l0.grassland_n1e1s1w1"
  1,  1, "t.l0.grassland_n0e1s1w1"
  1,  2, "t.l0.grassland_n1e0s1w1"
  1,  3, "t.l0.grassland_n0e0s1w1"
  1,  4, "t.l0.grassland_n1e1s0w1"
  1,  5, "t.l0.grassland_n0e1s0w1"
  1,  6, "t.l0.grassland_n1e0s0w1"
  1,  7, "t.l0.grassland_n0e0s0w1"
  1,  8, "t.l0.grassland_n1e1s1w0"
  1,  9, "t.l0.grassland_n0e1s1w0"
  1, 10, "t.l0.grassland_n1e0s1w0"
  1, 11, "t.l0.grassland_n0e0s1w0"
  1, 12, "t.l0.grassland_n1e1s0w0"
  1, 13, "t.l0.grassland_n0e1s0w0"
  1, 14, "t.l0.grassland_n1e0s0w0"
  1, 15, "t.l0.grassland_n0e0s0w0"

; Desert, and whether terrain to north, south, east, west 
; is more desert:

  2,  0, "t.l0.desert_n1e1s1w1"
  2,  1, "t.l0.desert_n0e1s1w1"
  2,  2, "t.l0.desert_n1e0s1w1"
  2,  3, "t.l0.desert_n0e0s1w1"
  2,  4, "t.l0.desert_n1e1s0w1"
  2,  5, "t.l0.desert_n0e1s0w1"
  2,  6, "t.l0.desert_n1e0s0w1"
  2,  7, "t.l0.desert_n0e0s0w1"
  2,  8, "t.l0.desert_n1e1s1w0"
  2,  9, "t.l0.desert_n0e1s1w0"
  2, 10, "t.l0.desert_n1e0s1w0"
  2, 11, "t.l0.desert_n0e0s1w0"
  2, 12, "t.l0.desert_n1e1s0w0"
  2, 13, "t.l0.desert_n0e1s0w0"
  2, 14, "t.l0.desert_n1e0s0w0"
  2, 15, "t.l0.desert_n0e0s0w0"

; Arctic, and whether terrain to north, south, east, west 
; is more arctic:

  3,  0, "t.l0.arctic_n1e1s1w1"
  3,  1, "t.l0.arctic_n0e1s1w1"
  3,  2, "t.l0.arctic_n1e0s1w1"
  3,  3, "t.l0.arctic_n0e0s1w1"
  3,  4, "t.l0.arctic_n1e1s0w1"
  3,  5, "t.l0.arctic_n0e1s0w1"
  3,  6, "t.l0.arctic_n1e0s0w1"
  3,  7, "t.l0.arctic_n0e0s0w1"
  3,  8, "t.l0.arctic_n1e1s1w0"
  3,  9, "t.l0.arctic_n0e1s1w0"
  3, 10, "t.l0.arctic_n1e0s1w0"
  3, 11, "t.l0.arctic_n0e0s1w0"
  3, 12, "t.l0.arctic_n1e1s0w0"
  3, 13, "t.l0.arctic_n0e1s0w0"
  3, 14, "t.l0.arctic_n1e0s0w0"
  3, 15, "t.l0.arctic_n0e0s0w0"

; Jungle, and whether terrain to north, south, east, west 
; is more jungle:

  4,  0, "t.l0.jungle_n1e1s1w1"
  4,  1, "t.l0.jungle_n0e1s1w1"
  4,  2, "t.l0.jungle_n1e0s1w1"
  4,  3, "t.l0.jungle_n0e0s1w1"
  4,  4, "t.l0.jungle_n1e1s0w1"
  4,  5, "t.l0.jungle_n0e1s0w1"
  4,  6, "t.l0.jungle_n1e0s0w1"
  4,  7, "t.l0.jungle_n0e0s0w1"
  4,  8, "t.l0.jungle_n1e1s1w0"
  4,  9, "t.l0.jungle_n0e1s1w0"
  4, 10, "t.l0.jungle_n1e0s1w0"
  4, 11, "t.l0.jungle_n0e0s1w0"
  4, 12, "t.l0.jungle_n1e1s0w0"
  4, 13, "t.l0.jungle_n0e1s0w0"
  4, 14, "t.l0.jungle_n1e0s0w0"
  4, 15, "t.l0.jungle_n0e0s0w0"

; Plains, and whether terrain to north, south, east, west 
; is more plains:

  5,  0, "t.l0.plains_n1e1s1w1"
  5,  1, "t.l0.plains_n0e1s1w1"
  5,  2, "t.l0.plains_n1e0s1w1"
  5,  3, "t.l0.plains_n0e0s1w1"
  5,  4, "t.l0.plains_n1e1s0w1"
  5,  5, "t.l0.plains_n0e1s0w1"
  5,  6, "t.l0.plains_n1e0s0w1"
  5,  7, "t.l0.plains_n0e0s0w1"
  5,  8, "t.l0.plains_n1e1s1w0"
  5,  9, "t.l0.plains_n0e1s1w0"
  5, 10, "t.l0.plains_n1e0s1w0"
  5, 11, "t.l0.plains_n0e0s1w0"
  5, 12, "t.l0.plains_n1e1s0w0"
  5, 13, "t.l0.plains_n0e1s0w0"
  5, 14, "t.l0.plains_n1e0s0w0"
  5, 15, "t.l0.plains_n0e0s0w0"

; Swamp, and whether terrain to north, south, east, west 
; is more swamp:

  6,  0, "t.l0.swamp_n1e1s1w1"
  6,  1, "t.l0.swamp_n0e1s1w1"
  6,  2, "t.l0.swamp_n1e0s1w1"
  6,  3, "t.l0.swamp_n0e0s1w1"
  6,  4, "t.l0.swamp_n1e1s0w1"
  6,  5, "t.l0.swamp_n0e1s0w1"
  6,  6, "t.l0.swamp_n1e0s0w1"
  6,  7, "t.l0.swamp_n0e0s0w1"
  6,  8, "t.l0.swamp_n1e1s1w0"
  6,  9, "t.l0.swamp_n0e1s1w0"
  6, 10, "t.l0.swamp_n1e0s1w0"
  6, 11, "t.l0.swamp_n0e0s1w0"
  6, 12, "t.l0.swamp_n1e1s0w0"
  6, 13, "t.l0.swamp_n0e1s0w0"
  6, 14, "t.l0.swamp_n1e0s0w0"
  6, 15, "t.l0.swamp_n0e0s0w0"

; Tundra, and whether terrain to north, south, east, west 
; is more tundra:

  7,  0, "t.l0.tundra_n1e1s1w1"
  7,  1, "t.l0.tundra_n0e1s1w1"
  7,  2, "t.l0.tundra_n1e0s1w1"
  7,  3, "t.l0.tundra_n0e0s1w1"
  7,  4, "t.l0.tundra_n1e1s0w1"
  7,  5, "t.l0.tundra_n0e1s0w1"
  7,  6, "t.l0.tundra_n1e0s0w1"
  7,  7, "t.l0.tundra_n0e0s0w1"
  7,  8, "t.l0.tundra_n1e1s1w0"
  7,  9, "t.l0.tundra_n0e1s1w0"
  7, 10, "t.l0.tundra_n1e0s1w0"
  7, 11, "t.l0.tundra_n0e0s1w0"
  7, 12, "t.l0.tundra_n1e1s0w0"
  7, 13, "t.l0.tundra_n0e1s0w0"
  7, 14, "t.l0.tundra_n1e0s0w0"
  7, 15, "t.l0.tundra_n0e0s0w0"

; Rivers (as special type), and whether north, south, east, west 
; also has river or is ocean:

 19,  0, "road.river_s_n0e0s0w0"
 19,  1, "road.river_s_n1e0s0w0"
 19,  2, "road.river_s_n0e1s0w0"
 19,  3, "road.river_s_n1e1s0w0"
 19,  4, "road.river_s_n0e0s1w0"
 19,  5, "road.river_s_n1e0s1w0"
 19,  6, "road.river_s_n0e1s1w0"
 19,  7, "road.river_s_n1e1s1w0"
 19,  8, "road.river_s_n0e0s0w1"
 19,  9, "road.river_s_n1e0s0w1"
 19, 10, "road.river_s_n0e1s0w1"
 19, 11, "road.river_s_n1e1s0w1"
 19, 12, "road.river_s_n0e0s1w1"
 19, 13, "road.river_s_n1e0s1w1"
 19, 14, "road.river_s_n0e1s1w1"
 19, 15, "road.river_s_n1e1s1w1"

; Ocean, and whether terrain to north, south, east, west 
; is more ocean (else shoreline)

 10, 12, "t.l0.coast1"

  9,  0, "t.l1.coast_n1e1s1w1"
  9,  1, "t.l1.coast_n0e1s1w1"
  9,  2, "t.l1.coast_n1e0s1w1"
  9,  3, "t.l1.coast_n0e0s1w1"
  9,  4, "t.l1.coast_n1e1s0w1"
  9,  5, "t.l1.coast_n0e1s0w1"
  9,  6, "t.l1.coast_n1e0s0w1"
  9,  7, "t.l1.coast_n0e0s0w1"
  9,  8, "t.l1.coast_n1e1s1w0"
  9,  9, "t.l1.coast_n0e1s1w0"
  9, 10, "t.l1.coast_n1e0s1w0"
  9, 11, "t.l1.coast_n0e0s1w0"
  9, 12, "t.l1.coast_n1e1s0w0"
  9, 13, "t.l1.coast_n0e1s0w0"
  9, 14, "t.l1.coast_n1e0s0w0"
  9, 15, "t.l1.coast_n0e0s0w0"

 10, 13, "t.l0.floor1"

  9,  0, "t.l1.floor_n1e1s1w1"
  9,  1, "t.l1.floor_n0e1s1w1"
  9,  2, "t.l1.floor_n1e0s1w1"
  9,  3, "t.l1.floor_n0e0s1w1"
  9,  4, "t.l1.floor_n1e1s0w1"
  9,  5, "t.l1.floor_n0e1s0w1"
  9,  6, "t.l1.floor_n1e0s0w1"
  9,  7, "t.l1.floor_n0e0s0w1"
  9,  8, "t.l1.floor_n1e1s1w0"
  9,  9, "t.l1.floor_n0e1s1w0"
  9, 10, "t.l1.floor_n1e0s1w0"
  9, 11, "t.l1.floor_n0e0s1w0"
  9, 12, "t.l1.floor_n1e1s0w0"
  9, 13, "t.l1.floor_n0e1s0w0"
  9, 14, "t.l1.floor_n1e0s0w0"
  9, 15, "t.l1.floor_n0e0s0w0"

 10, 14, "t.l0.inaccessible1"

; For hills, forest and mountains don't currently have a full set,
; re-use values but provide for future expansion; current sets
; effectively ignore N/S terrain.

; Hills, and whether terrain to north, south, east, west 
; is more hills.

 10,  0, "t.l0.hills_n0e0s0w0",  ; not-hills E and W
         "t.l0.hills_n0e0s1w0", 
         "t.l0.hills_n1e0s0w0", 
         "t.l0.hills_n1e0s1w0" 
 10,  1, "t.l0.hills_n0e1s0w0",  ; hills E
         "t.l0.hills_n0e1s1w0", 
         "t.l0.hills_n1e1s0w0", 
         "t.l0.hills_n1e1s1w0" 
 10,  2, "t.l0.hills_n0e1s0w1",  ; hills E and W
         "t.l0.hills_n0e1s1w1", 
         "t.l0.hills_n1e1s0w1", 
         "t.l0.hills_n1e1s1w1" 
 10,  3, "t.l0.hills_n0e0s0w1",  ; hills W
         "t.l0.hills_n0e0s1w1", 
         "t.l0.hills_n1e0s0w1", 
         "t.l0.hills_n1e0s1w1" 

; Forest, and whether terrain to north, south, east, west 
; is more forest.

 10,  4, "t.l0.forest_n0e0s0w0",  ; not-forest E and W
         "t.l0.forest_n0e0s1w0", 
         "t.l0.forest_n1e0s0w0", 
         "t.l0.forest_n1e0s1w0" 
 10,  5, "t.l0.forest_n0e1s0w0",  ; forest E
         "t.l0.forest_n0e1s1w0", 
         "t.l0.forest_n1e1s0w0", 
         "t.l0.forest_n1e1s1w0" 
 10,  6, "t.l0.forest_n0e1s0w1",  ; forest E and W
         "t.l0.forest_n0e1s1w1", 
         "t.l0.forest_n1e1s0w1", 
         "t.l0.forest_n1e1s1w1" 
 10,  7, "t.l0.forest_n0e0s0w1",  ; forest W
         "t.l0.forest_n0e0s1w1", 
         "t.l0.forest_n1e0s0w1", 
         "t.l0.forest_n1e0s1w1" 

; Mountains, and whether terrain to north, south, east, west 
; is more mountains.

 10,  8, "t.l0.mountains_n0e0s0w0",  ; not-mountains E and W
         "t.l0.mountains_n0e0s1w0", 
         "t.l0.mountains_n1e0s0w0", 
         "t.l0.mountains_n1e0s1w0" 
 10,  9, "t.l0.mountains_n0e1s0w0",  ; mountains E
         "t.l0.mountains_n0e1s1w0", 
         "t.l0.mountains_n1e1s0w0", 
         "t.l0.mountains_n1e1s1w0" 
 10, 10, "t.l0.mountains_n0e1s0w1",  ; mountains E and W
         "t.l0.mountains_n0e1s1w1", 
         "t.l0.mountains_n1e1s0w1", 
         "t.l0.mountains_n1e1s1w1" 
 10, 11, "t.l0.mountains_n0e0s0w1",  ; mountains W
         "t.l0.mountains_n0e0s1w1", 
         "t.l0.mountains_n1e0s0w1", 
         "t.l0.mountains_n1e0s1w1" 

; Darkness (unexplored) to north, south, east, west 

 13,  1, "tx.darkness_n1e0s0w0"
 13,  2, "tx.darkness_n0e1s0w0"
 13,  3, "tx.darkness_n1e1s0w0"
 13,  4, "tx.darkness_n0e0s1w0"
 13,  5, "tx.darkness_n1e0s1w0"
 13,  6, "tx.darkness_n0e1s1w0"
 13,  7, "tx.darkness_n1e1s1w0"
 13,  8, "tx.darkness_n0e0s0w1"
 13,  9, "tx.darkness_n1e0s0w1"
 13, 10, "tx.darkness_n0e1s0w1"
 13, 11, "tx.darkness_n1e1s0w1"
 13, 12, "tx.darkness_n0e0s1w1"
 13, 13, "tx.darkness_n1e0s1w1"
 13, 14, "tx.darkness_n0e1s1w1"
 13, 15, "tx.darkness_n1e1s1w1"

; River outlets, river to north, south, east, west 

  8, 16, "road.river_outlet_n"
  8, 17, "road.river_outlet_w"
  8, 18, "road.river_outlet_s"
  8, 19, "road.river_outlet_e"

; Terrain special resources:

 11,  0, "ts.seals"
 11,  1, "ts.oasis"
 11,  2, "ts.forest_game"
 11,  3, "ts.grassland_resources"
 11,  4, "ts.coal"
 11,  5, "ts.gems"
 11,  6, "ts.gold"
 11,  7, "ts.fish"
 11,  8, "ts.horses"
 11,  9, "ts.river_resources"
 11, 10, "ts.oil", "ts.arctic_oil"
 11, 11, "ts.tundra_game"

  5, 16, "ts.spice"
  5, 17, "ts.furs"
  5, 18, "ts.peat"
  5, 19, "ts.arctic_ivory"

  6, 16, "ts.fruit"
  6, 17, "ts.iron"
  6, 18, "ts.whales"
  6, 19, "ts.wheat"

  7, 16, "ts.pheasant"
  7, 17, "ts.buffalo"
  7, 18, "ts.silk"
  7, 19, "ts.wine"

; Terrain improvements and similar:

 12,  7, "tx.farmland"
 12,  8, "tx.irrigation"
 12,  9, "tx.mine"
 12, 10, "tx.oil_mine"
 12, 11, "tx.pollution"
 12, 12, "base.buoy_mg"
 12, 13, "base.ruins_mg"
 12, 14, "tx.village"
 12, 15, "base.fortress_bg"
 13, 16, "base.airbase_mg"
 13, 0,  "mask.tile"
 13, 17, "tx.fog"
 13, 18, "tx.fallout"

; Unit activity letters:  (note unit icons have just "u.")

  9, 18, "unit.auto_attack",
         "unit.auto_settler"
  9, 19, "unit.stack"
 10, 18, "unit.connect"
 10, 19, "unit.auto_explore"
 11, 12, "unit.transform"
 11, 13, "unit.sentry"
 11, 14, "unit.goto"
 11, 15, "unit.mine"
 11, 16, "unit.pollution"
 11, 17, "unit.road"
 11, 18, "unit.irrigate"
 11, 19, "unit.fortifying",
         "unit.fortress"
 12, 16, "unit.airbase"
 12, 17, "unit.pillage"
 12, 18, "unit.fortified"
 12, 19, "unit.fallout"
 13, 19, "unit.patrol"
 19, 16, "unit.lowfuel"
 19, 16, "unit.tired"
 19, 17, "unit.loaded"
 10, 18, "unit.convert"

; Unit hit-point bars: approx percent of hp remaining

 17,  0, "unit.hp_100"
 17,  1, "unit.hp_90"
 17,  2, "unit.hp_80"
 17,  3, "unit.hp_70"
 17,  4, "unit.hp_60"
 17,  5, "unit.hp_50"
 17,  6, "unit.hp_40"
 17,  7, "unit.hp_30"
 17,  8, "unit.hp_20"
 17,  9, "unit.hp_10"
 17, 10, "unit.hp_0"

; Numbers: city size: (also used for goto)

 14,  0, "city.size_0"
 14,  1, "city.size_1"
 14,  2, "city.size_2"
 14,  3, "city.size_3"
 14,  4, "city.size_4"
 14,  5, "city.size_5"
 14,  6, "city.size_6"
 14,  7, "city.size_7"
 14,  8, "city.size_8"
 14,  9, "city.size_9"
 14, 10, "city.size_00"
 14, 11, "city.size_10"
 14, 12, "city.size_20"
 14, 13, "city.size_30"
 14, 14, "city.size_40"
 14, 15, "city.size_50"
 14, 16, "city.size_60"
 14, 17, "city.size_70"
 14, 18, "city.size_80"
 14, 19, "city.size_90"
 15,  1, "city.size_100"
 15,  2, "city.size_200"
 15,  3, "city.size_300"
 15,  4, "city.size_400"
 15,  5, "city.size_500"
 15,  6, "city.size_600"
 15,  7, "city.size_700"
 15,  8, "city.size_800"
 15,  9, "city.size_900"

; Numbers: city tile food/shields/trade y/g/b

 18,  0, "city.t_food_0"
 18,  1, "city.t_food_1"
 18,  2, "city.t_food_2"
 18,  3, "city.t_food_3"
 18,  4, "city.t_food_4"
 18,  5, "city.t_food_5"
 18,  6, "city.t_food_6"
 18,  7, "city.t_food_7"
 18,  8, "city.t_food_8"
 18,  9, "city.t_food_9"

; Veteran Levels: up to 9 military honors for experienced units

 18, 11, "unit.vet_1"
 18, 12, "unit.vet_2"
 18, 13, "unit.vet_3"
 18, 14, "unit.vet_4"
 18, 15, "unit.vet_5"
 18, 16, "unit.vet_6"
 18, 17, "unit.vet_7"
 18, 18, "unit.vet_8"
 18, 19, "unit.vet_9"

 16,  0, "city.t_shields_0"
 16,  1, "city.t_shields_1"
 16,  2, "city.t_shields_2"
 16,  3, "city.t_shields_3"
 16,  4, "city.t_shields_4"
 16,  5, "city.t_shields_5"
 16,  6, "city.t_shields_6"
 16,  7, "city.t_shields_7"
 16,  8, "city.t_shields_8"
 16,  9, "city.t_shields_9"

 16, 10, "city.t_trade_0"
 16, 11, "city.t_trade_1"
 16, 12, "city.t_trade_2"
 16, 13, "city.t_trade_3"
 16, 14, "city.t_trade_4"
 16, 15, "city.t_trade_5"
 16, 16, "city.t_trade_6"
 16, 17, "city.t_trade_7"
 16, 18, "city.t_trade_8"
 16, 19, "city.t_trade_9"

; Unit upkeep in city dialog:
; These should probably be handled differently and have
; a different size...

 17, 12, "upkeep.gold"
 17, 13, "upkeep.gold2"
 17, 15, "upkeep.food"
 17, 16, "upkeep.food2"
 17, 17, "upkeep.unhappy"
 17, 18, "upkeep.unhappy2"
 17, 19, "upkeep.shield"

; Misc:

  9, 17, "user.attention"	; Variously crosshair/red-square/arrows

}

[grid_nuke]

x_top_left = 510
y_top_left = 30
dx = 90
dy = 90

tiles = { "row", "column", "tag"
  0, 0, "explode.nuke"
}

[grid_ocean]
x_top_left = 0
y_top_left = 0
dx = 15
dy = 15

tiles = {"row", "column", "tag"

; coast cell sprites.  See doc/README.graphics
  0,  0, "t.l2.coast_cell_u010"
  0,  1, "t.l2.coast_cell_r010"
  1,  0, "t.l2.coast_cell_l010"
  1,  1, "t.l2.coast_cell_d010"

  0,  2, "t.l2.coast_cell_u000"
  0,  2, "t.l2.coast_cell_u001"
  0,  2, "t.l2.coast_cell_u011"
  0,  2, "t.l2.coast_cell_u100"
  0,  2, "t.l2.coast_cell_u101"
  0,  2, "t.l2.coast_cell_u110"
  0,  2, "t.l2.coast_cell_u111"

  0,  2, "t.l2.coast_cell_l000"
  0,  2, "t.l2.coast_cell_l001"
  0,  2, "t.l2.coast_cell_l011"
  0,  2, "t.l2.coast_cell_l100"
  0,  2, "t.l2.coast_cell_l101"
  0,  2, "t.l2.coast_cell_l110"
  0,  2, "t.l2.coast_cell_l111"

  0,  2, "t.l2.coast_cell_r000"
  0,  2, "t.l2.coast_cell_r001"
  0,  2, "t.l2.coast_cell_r011"
  0,  2, "t.l2.coast_cell_r100"
  0,  2, "t.l2.coast_cell_r101"
  0,  2, "t.l2.coast_cell_r110"
  0,  2, "t.l2.coast_cell_r111"

  0,  2, "t.l2.coast_cell_d000"
  0,  2, "t.l2.coast_cell_d001"
  0,  2, "t.l2.coast_cell_d011"
  0,  2, "t.l2.coast_cell_d100"
  0,  2, "t.l2.coast_cell_d101"
  0,  2, "t.l2.coast_cell_d110"
  0,  2, "t.l2.coast_cell_d111"

; Deep Ocean fallback to Ocean tiles
  0,  0, "t.l2.floor_cell_u010"
  0,  1, "t.l2.floor_cell_r010"
  1,  0, "t.l2.floor_cell_l010"
  1,  1, "t.l2.floor_cell_d010"

  0,  2, "t.l2.floor_cell_u000"
  0,  2, "t.l2.floor_cell_u001"
  0,  2, "t.l2.floor_cell_u011"
  0,  2, "t.l2.floor_cell_u100"
  0,  2, "t.l2.floor_cell_u101"
  0,  2, "t.l2.floor_cell_u110"
  0,  2, "t.l2.floor_cell_u111"

  0,  2, "t.l2.floor_cell_l000"
  0,  2, "t.l2.floor_cell_l001"
  0,  2, "t.l2.floor_cell_l011"
  0,  2, "t.l2.floor_cell_l100"
  0,  2, "t.l2.floor_cell_l101"
  0,  2, "t.l2.floor_cell_l110"
  0,  2, "t.l2.floor_cell_l111"

  0,  2, "t.l2.floor_cell_r000"
  0,  2, "t.l2.floor_cell_r001"
  0,  2, "t.l2.floor_cell_r011"
  0,  2, "t.l2.floor_cell_r100"
  0,  2, "t.l2.floor_cell_r101"
  0,  2, "t.l2.floor_cell_r110"
  0,  2, "t.l2.floor_cell_r111"

  0,  2, "t.l2.floor_cell_d000"
  0,  2, "t.l2.floor_cell_d001"
  0,  2, "t.l2.floor_cell_d011"
  0,  2, "t.l2.floor_cell_d100"
  0,  2, "t.l2.floor_cell_d101"
  0,  2, "t.l2.floor_cell_d110"
  0,  2, "t.l2.floor_cell_d111"

}
