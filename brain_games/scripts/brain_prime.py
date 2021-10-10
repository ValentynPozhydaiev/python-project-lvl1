#!/usr/bin/env python3

"""The module contains the main executable script."""

from brain_games.game_template import game_template
from brain_games.games.game_prime import game_prime_logic, game_prime_rules
from brain_games.welcome_func import greet, welcome_user


def main():
    """Run the main script.

    Arguments:
        No input required.
    """
    greet()
    user_name = welcome_user()
    game_template(user_name, game_prime_rules, game_prime_logic)


if __name__ == '__main__':
    main()
