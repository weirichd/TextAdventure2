from random import random

from menu import menu
from monster import monsters, get_monster
from hero import level_up, display_stats


def monster_menu(hero):
    print('What monster will you fight?')
    monster_list = list(monsters.keys())
    monster_list.append('Go back')

    monster_choice = menu(monster_list)

    if monster_choice != 'Go back':
        monster = get_monster(monster_choice)
        battle(hero, monster)

        if hero['hp'] > 0:
            print('{} defeated the {}.'.format(hero['name'], monster['name']))
            hero['exp'] = hero['exp'] + monster['exp']
            print('{} got {} exp.'.format(hero['name'], monster['exp']))
            if hero['exp'] >= hero['next level']:
                hero = level_up(hero)
                print('{} reached level {}.'.format(hero['name'], hero['level']))
                display_stats(hero)
        else:
            print('{} died...'.format(hero['name']))
            return True  # Game over

    return False


def battle(hero, monster):
    if hero['speed'] < monster['speed']:
        first = monster
        second = hero
    elif hero['speed'] > monster['speed']:
        first = hero
        second = monster
    else:  # When speed is tied, we flip a coin.
        if random() > 0.5:
            first = monster
            second = hero
        else:
            first = hero
            second = monster

    battle_over = False
    run_successful = False
    while not (battle_over or run_successful):
        display_battle_status(hero, monster)
        action = menu(['Attack', 'Run'])

        if action == 'Attack':
            attack(first, second)

            if second['hp'] > 0:
                attack(second, first)

            if hero['hp'] == 0 or monster['hp'] == 0:
                battle_over = True

        if action == 'Run':
            run_successful = True


def attack(attacker, target):
    if attacker['weapon'] is None:
        print('{} attacks {}!'.format(attacker['name'], target['name']))
    else:
        print('{} {} their {} at {}!'.format(
            attacker['name'],
            attacker['weapon']['verb'],
            attacker['weapon']['name'],
            target['name']))

    weapon_bonus = 0
    if attacker['weapon'] is not None:
        weapon_bonus = attacker['weapon']['damage']

    base_damage = attacker['attack'] + weapon_bonus - target['defense']

    if base_damage <= 0:
        base_damage = 1

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
        print('{} missed!'.format(attacker['name']))
    else:
        if special == 'critical':
            print('{} landed a critical hit!'.format(attacker['name']))
        print('It did {} damage!'.format(damage))


def display_battle_status(hero, monster):
    print('+-----------------+-----------------+')
    print('|  {0: <13}  |  {1: <13}  |'.format(hero['name'], monster['name']))
    print('|  HP: {0: >4}/{1: <4}  |  HP: {2: >4}/{3: <4}  |'.format(
        hero['hp'], hero['max hp'], monster['hp'], monster['max hp']))
    print('+-----------------+-----------------+')
