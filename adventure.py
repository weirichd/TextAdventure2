from menu import menu
from hero import create_new_hero, hero_classes, display_stats, inventory
from battle import monster_menu


def main():
    print('Welcome to Adventure II:')
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
        action = menu(['Display Stats', 'Inventory', 'Battle', 'Quit Game'])

        if action == 'Display Stats':
            display_stats(hero)
        if action == 'Battle':
            game_over = monster_menu(hero)
            if game_over:
                quit_game = True

        if action == 'Inventory':
            inventory(hero)

        if action == 'Quit Game':
            quit_game = True

    if game_over:
        print('GAME OVER')

    print('Thanks for playing.')


def new_game():
    print('New Game')
    print('What is your name?')

    name = input()

    print('Please select a class.')

    selected_class = menu(list(hero_classes.keys()))

    return create_new_hero(name, selected_class)


def load_character():
    print('Saving not implemented yet. Starting a new game.')
    return new_game()


if __name__ == '__main__':
    main()