hero_classes = {
    'Warrior': {
        'max hp': 12,
        'attack': 3,
        'defense': 2,
        'hp per level': 2,
        'attack per level': 3,
        'defense per level': 2
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
        'name': 'Sword',
        'verb': 'swings',
        'damage': 2
    }

    return hero


def display_stats(hero):
    print('+-----------------+----------------+')
    print('|  {0: <13}  |  {1: <10}    |'.format(hero['name'], hero['class']))
    print('|  HP: {0: >4}/{1: <4}  |  LEVEL {2: <3}     |'.format(hero['hp'], hero['max hp'], hero['level']))
    print('|  EXP: {0: <6}    |  NEXT: {1: <6}  |'.format(hero['exp'], hero['next level']))
    print('+-----------------+----------------+')
    print('|  ATTACK:        |  {0: <4}          |'.format(hero['attack']))
    print('|  DEFENSE:       |  {0: <4}          |'.format(hero['defense']))
    print('+-----------------+----------------+')


def level_up(hero):
    hero['level'] = hero['level'] + 1
    hero['max hp'] = hero['max hp'] + hero_classes[hero['class']]['hp per level']
    hero['hp'] = hero['max hp']
    hero['attack'] = hero['attack'] + hero_classes[hero['class']]['attack per level']
    hero['defense'] = hero['defense'] + hero_classes[hero['class']]['defense per level']
    hero['next level'] = hero['next level'] + hero['level'] * 2

    return hero
