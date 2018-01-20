from random import random

from menu import menu


def battle(hero, monster):
    battle_over = False
    run_successful = False
    player_won = False
    while not (battle_over or run_successful):
        display_battle_status(hero, monster)
        action = menu(['Attack', 'Run'])

        if action == 'Attack':
            monster, damage, special = attack(hero, monster)
            print('{} attacks the {}!'.format(hero['name'], monster['name']))
            # TODO: delay here
            if special == 'miss':
                print('Oh no, it missed!')
            else:
                if special == 'critical':
                    print('{} landed a critical hit!'.format(hero['name']))
                print('It did {} damage!'.format(damage))

            if monster['hp'] > 0:
                hero, damage, special = attack(monster, hero)
                print('The {} attacks {}!'.format(monster['name'], hero['name']))
                # TODO: delay here
                if special == 'miss':
                    print('The attack missed!')
                else:
                    if special == 'critical':
                        print('The {} landed a critical hit!'.format(monster['name']))
                    print('It did {} damage!'.format(damage))
                    if hero['hp'] == 0:
                        battle_over = True
                        player_won = False

            else:
                print('{} defeated the monster!')
                player_won = True
                battle_over = True

        if action == 'Run':
            run_successful = True

    if battle_over:
        if player_won:
            print('You won.')
        else:
            print('You lost.')


def attack(attacker, target):
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

    return target, damage, special


def display_battle_status(hero, monster):
    print('{}: {} HP - {}: {} HP'.format(hero['name'], hero['hp'], monster['name'], monster['hp']))
