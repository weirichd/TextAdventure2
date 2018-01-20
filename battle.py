from random import random

from menu import menu


def battle(hero, monster):
    battle_over = False
    run_successful = False
    while not (battle_over or run_successful):
        display_battle_status(hero, monster)
        action = menu(['Attack', 'Run'])

        if action == 'Attack':

            first = hero
            second = monster

            second = attack(first, second)

            if second['hp'] > 0:
                hero = attack(second, first)

            if hero['hp'] == 0 or monster['hp'] == 0:
                battle_over = True

        if action == 'Run':
            run_successful = True


def attack(attacker, target):
    print('{} attacks {}!'.format(attacker['name'], target['name']))

    attack_stat = attacker['attack']
    defense_stat = target['defense']

    weapon_bonus = 0
    if attacker['weapon'] is not None:
        weapon_bonus = attacker['weapon']['damage']

    base_damage = attack_stat + weapon_bonus - defense_stat

    if base_damage < 0:
        base_damage = 0

    modifier = 1
    special = None
    random_number = random()

    if random_number < 0.1:
        modifier = 0
        special = 'miss'
    elif random_number < 0.2:
        modifier = 2
        special = 'critical'

    damage = base_damage * modifier
    target['hp'] = target['hp'] - damage
    if target['hp'] < 0:
        target['hp'] = 0

    if special == 'miss':
        print('Oh no, it missed!')
    else:
        if special == 'critical':
            print('{} landed a critical hit!'.format(attacker['name']))
        print('It did {} damage!'.format(damage))

    return target


def display_battle_status(hero, monster):
    print('+-----------------+-----------------+')
    print('|  {0: <13}  |  {1: <13}  |'.format(hero['name'], monster['name']))
    print('|  HP: {0: >4}/{1: <4}  |  HP: {2: >4}/{3: <4}  |'.format(
        hero['hp'], hero['max hp'], monster['hp'], monster['max hp']))
    print('+-----------------+-----------------+')
