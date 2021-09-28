#!/usr/bin/env python3

"""The module contains the main executable script."""

from brain_games.game_template import guess_even_number
from brain_games.welcome_func import greet, welcome_user


def main():
    """Run the main script.

    Arguments:
        No input required.
    """
    greet()
    user_name = welcome_user()
    guess_even_number(user_name)


if __name__ == '__main__':
    main()
