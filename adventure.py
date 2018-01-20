from menu import menu

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


def main():
    print('Welcome to Adventure II!')

    print('Select an option:')

    option = menu(['New Game', 'Load Saved Game'])

    if option == 'Load Saved Game':
        hero = load_character()
    else:
        hero = new_game()

    # TODO: For debug use
    print(hero)

    quit_game = False

    while not quit_game:
        action = menu(['Quit Game'])

        if action == 'Quit Game':
            quit_game = True

    print('Thanks for playing.')


def new_game():
    print('...')
    print('What is your name?')

    hero = dict()

    hero['name'] = input()

    print('Please select a class.')

    selected_class = menu(list(hero_classes.keys()))

    hero['class'] = selected_class
    hero['max_hp'] = hero_classes[selected_class]['hp']
    hero['hp'] = hero['max_hp']
    hero['attack'] = hero_classes[selected_class]['attack']
    hero['defense'] = hero_classes[selected_class]['defense']

    return hero


def load_character():
    print('Saving not implemented yet. Starting a new game.')
    return new_game()


if __name__ == '__main__':
    main()