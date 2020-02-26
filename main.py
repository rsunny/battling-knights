from base_classes.knight import Knight
from base_classes.weapon import Weapon
from helper import process_knight
from io_helper import get_input, make_output


def setup():
    knights = {
        'R': Knight(0, 0, 'red'),
        'B': Knight(7, 0, 'blue'),
        'G': Knight(7, 7, 'green'),
        'Y': Knight(0, 7, 'yellow')
    }
    weapons = {
        'Axe': Weapon(2, 0, 2, 2, 'axe'),
        'MagicStaff': Weapon(1, 1, 5, 2, 'magic_staff'),
        'Dagger': Weapon(1, 0, 2, 5, 'dagger'),
        'Helmet': Weapon(0, 1, 5, 5, 'helmet')
    }
    return knights, weapons


def play_game():
    knights, weapons = setup()
    for knight, direction in get_input():
        process_knight(knight, direction, knights, weapons)
    make_output(knights, weapons)


if __name__ == '__main__':
    play_game()
