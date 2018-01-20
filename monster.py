monsters = {
    'Giant Rat': {
        'max hp': 10,
        'attack': 3,
        'defense': 1,
        'weapon': None
    }
}


def get_monster(type):
    monster = monsters[type].copy()
    monster['name'] = type
    monster['hp'] = monster['max hp']

    return monster
