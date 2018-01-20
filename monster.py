monsters = {
    'Giant Rat': {
        'max hp': 10,
        'attack': 3,
        'defense': 1,
        'speed': 1,
        'weapon': None,
        'exp': 1
    },
    'Troll': {
        'max hp': 15,
        'attack': 5,
        'defense': 3,
        'speed': 3,
        'weapon': None,
        'exp': 2
    },
    'Ogre': {
        'max hp': 25,
        'attack': 7,
        'defense': 5,
        'speed': 5,
        'weapon': None,
        'exp': 3
    }
}


def get_monster(monster_type):
    monster = monsters[monster_type].copy()
    monster['name'] = monster_type
    monster['hp'] = monster['max hp']

    return monster
