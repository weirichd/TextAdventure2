from menu import menu
from hero import create_new_hero, hero_classes, display_stats
from battle import battle

troll = {
    'name': 'Troll',
    'hp': 10,
    'attack': 5,
    'defense': 1,
    'weapon': None
}


def main():
    print('Welcome to Adventure II!')

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
            battle(hero, troll)

            if hero['hp'] == 0:
                print('You have died.')
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