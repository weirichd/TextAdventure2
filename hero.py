hero_classes = {
    'Warrior': {
        'hp': 12,
        'attack': 3,
        'defense': 2,
        'hp per level': 2,
        'attack per level': 3,
        'defense per level': 2
    }
}


def create_new_hero(name, hero_class):
    hero = dict()

    hero['name'] = name
    hero['level'] = 1
    hero['class'] = hero_class
    hero['max_hp'] = hero_classes[hero_class]['hp']
    hero['hp'] = hero['max_hp']
    hero['attack'] = hero_classes[hero_class]['attack']
    hero['defense'] = hero_classes[hero_class]['defense']

    return hero


def display_stats(hero):

    print('Name ' + hero['name'])
    print('Class ' + hero['class'])

    print('+-----------------+--------------+')
    print('|  {0: <10}     |  {1: <10}  |'.format(hero['name'], hero['class']))
    print('|  HP: {0: >4}/{1: <4}  |  Level {2: <3}   |'.format(hero['hp'], hero['max_hp'], hero['level']))
    print('+-----------------+--------------+')
    print('|  ATTACK:        |  {0: <4}        |'.format(hero['attack']))
    print('|  DEFENSE:       |  {0: <4}        |'.format(hero['defense']))
    print('+-----------------+--------------+')
