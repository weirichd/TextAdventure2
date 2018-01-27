hero_classes = {
    'Warrior': {
        'max hp': 12,
        'attack': 3,
        'defense': 2,
        'speed': 0,
        'hp per level': 2,
        'attack per level': 3,
        'defense per level': 2,
        'speed per level': 1
    },
    'Archer': {
        'max hp': 8,
        'attack': 5,
        'defense': 1,
        'speed': 2,
        'hp per level': 2,
        'attack per level': 4,
        'defense per level': 1,
        'speed per level': 1
    }
}


def create_new_hero(name, hero_class):
    hero = hero_classes[hero_class].copy()

    hero['name'] = name
    hero['class'] = hero_class
    hero['level'] = 1
    hero['exp'] = 0
    hero['next level'] = 3
    hero['hp'] = hero['max hp']
    hero['weapon'] = {
        'name': 'rusty sword',
        'verb': 'swings',
        'damage': 2
    }
    hero['inventory'] = ['Potion', 'Feather']
    hero['gold'] = 0

    return hero


def display_stats(hero):
    print('+-----------------+----------------+')
    print('|  {0: <13}  |  {1: <10}    |'.format(hero['name'], hero['class']))
    print('|  HP: {0: >4}/{1: <4}  |  LEVEL {2: <3}     |'.format(hero['hp'], hero['max hp'], hero['level']))
    print('|  EXP: {0: <6}    |  NEXT: {1: <6}  |'.format(hero['exp'], hero['next level']))
    print('+-----------------+----------------+')
    print('|  ATTACK:        |  {0: <4}          |'.format(hero['attack']))
    print('|  DEFENSE:       |  {0: <4}          |'.format(hero['defense']))
    print('|  SPEED:         |  {0: <4}          |'.format(hero['speed']))
    print('+-----------------+----------------+')


def level_up(hero):
    hero['level'] = hero['level'] + 1
    hero['max hp'] = hero['max hp'] + hero['hp per level']
    hero['hp'] = hero['max hp']
    hero['attack'] = hero['attack'] + hero['attack per level']
    hero['defense'] = hero['defense'] + hero['defense per level']
    hero['speed'] = hero['speed'] + hero['speed per level']
    hero['next level'] = hero['next level'] + hero['level'] * 2

    return hero


def inventory(hero):
    print("{}'s Inventory:".format(hero['name']))
    print('Gold: {}'.format(hero['gold']))
    for item in hero['inventory']:
        print(item)
