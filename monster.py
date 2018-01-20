monsters = {
    'Giant Rat': {
        'max hp': 10,
        'attack': 3,
        'defense': 1,
        'speed': 1,
        'weapon': None,
        'exp': 1
    },
}


def get_monster(monster_type):
    monster = monsters[monster_type].copy()
    monster['name'] = monster_type
    monster['hp'] = monster['max hp']

    return monster
