#!/usr/bin/env python3

"""The module contains the main executable script."""

from brain_games.game_template import game_template
from brain_games.games.game_progression import (
    game_progression_logic,
    game_progression_rules,
)
from brain_games.welcome_func import greet, welcome_user


def main():
    """Run the main script.

    Arguments:
        No input required.
    """
    greet()
    user_name = welcome_user()
    game_template(user_name, game_progression_rules, game_progression_logic)


if __name__ == '__main__':
    main()
