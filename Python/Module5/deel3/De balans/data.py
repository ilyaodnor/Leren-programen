#constants
JOURNEY_IN_DAYS = 11
COST_FOOD_HUMAN_COPPER_PER_DAY = 4
COST_FOOD_HORSE_COPPER_PER_DAY = 3

COST_TENT_GOLD_PER_WEEK = 3
COST_HORSE_SILVER_PER_DAY = 5

#data

mainCharacter = {
    'name' : 'Ilya',
    'ownsHorse' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 1,
        'silver' : 7,
        'copper' : 5
    }
}

friends = [{
    'name' : 'Jorick',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 9,
        'silver' : 9,
        'copper' : 43
    }
},{
    'name' : 'Grommel',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 1,
        'gold' : 2,
        'silver' : 2,
        'copper' : 8
    }
},{
    'name' : 'Tristan',
    'shareWith' : False,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 2,
        'silver' : 17,
        'copper' : 11
    }
},{
    'name' : 'Massimo',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 5,
        'silver' : 9,
        'copper' : 3
    }
},{
    'name' : 'Durbane',
    'shareWith' : True,
    'adventuring' : False,
    'cash' : {
        'platinum' : 1,
        'gold' : 5,
        'silver' : 12,
        'copper' : 11
    }
},{
    'name' : 'Otho',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 1,
        'silver' : 2,
        'copper' : 7
    }
}]

adventurerGear = [{
    'name' : 'Lantaren',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Lampenolie',
    'amount' : 2,
    'unit' : 'dl',
    'price' : {
        'amount' : 13,
        'type' : 'copper'
    }
},{
    'name' : 'Hengel',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
},{
    'name' : 'Schop',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Tinderbox',
    'amount' : 3,
    'unit' : 'x',
    'price' : {
        'amount' : 8,
        'type' : 'copper'
    }
},{
    'name' : 'Rugzak',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 13,
        'type' : 'silver'
    }
},{
    'name' : 'Touw',
    'amount' : 3,
    'unit' : 'meter',
    'price' : {
        'amount' : 14,
        'type' : 'silver'
    }
},{
    'name' : 'Fakkel',
    'amount' : 2,
    'unit' : 'x',
    'price' : {
        'amount' : 12,
        'type' : 'silver'
    }
},{
    'name' : 'Waterzak',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 11,
        'type' : 'silver'
    }
}]

investors = []

treasure = []