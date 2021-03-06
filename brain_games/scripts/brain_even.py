#!/usr/bin/env python3

"""The module contains the main executable script."""

from brain_games.game_template import game_template
from brain_games.games.game_even import game_even_logic, game_even_rules
from brain_games.welcome_func import greet, welcome_user


def main():
    """Run the main script.

    Arguments:
        No input required.
    """
    greet()
    user_name = welcome_user()
    game_template(user_name, game_even_rules, game_even_logic)


if __name__ == '__main__':
    main()
