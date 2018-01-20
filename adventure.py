from menu import menu
from hero import create_new_hero, hero_classes, display_stats, level_up
from battle import battle
from monster import get_monster, monsters


def main():
    print('Welcome to '
          'Adventure II:')
    print('The Adventure Continues')

    print('Select an option:')

    option = menu(['New Game', 'Load Saved Game'])

    if option == 'Load Saved Game':
        hero = load_character()
    else:
        hero = new_game()

    quit_game = False
    game_over = False

    while not quit_game:
        action = menu(['Display Stats', 'Battle', 'Quit Game'])

        if action == 'Display Stats':
            display_stats(hero)
        if action == 'Battle':
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
                    game_over = True
                    quit_game = True

        if action == 'Quit Game':
            quit_game = True

    if game_over:
        print('GAME OVER')

    print('Thanks for playing.')


def new_game():
    print('New Game')
    print('What is your name?')

    # TODO: Warn about name length
    name = input()

    print('Please select a class.')

    selected_class = menu(list(hero_classes.keys()))

    return create_new_hero(name, selected_class)


def load_character():
    print('Saving not implemented yet. Starting a new game.')
    return new_game()


if __name__ == '__main__':
    main()