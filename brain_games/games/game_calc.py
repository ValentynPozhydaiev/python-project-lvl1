"""The module contains the logic of the "Calculator" game."""

from random import choice, randint


def game_calc_logic():
    """Provide the puzzle and the answer.

    Argiments:
        No input required.

    Returns:
        A tuple containing the puzzle and the correct answer.
    """
    first_rand = randint(1, 20)
    second_rand = randint(1, 20)

    quest = [
        '{0} + {1}'.format(str(first_rand), str(second_rand)),
        '{0} - {1}'.format(str(first_rand), str(second_rand)),
        '{0} * {1}'.format(str(first_rand), str(second_rand)),
    ]
    ops = [
        str(first_rand + second_rand),
        str(first_rand - second_rand),
        str(first_rand * second_rand),
    ]

    return choice(list(zip(quest, ops)))


def game_calc_rules():
    """Print the game rule to the user.

    Arguments:
        No input required.

    Returns:
        The game rule as a string.
    """
    return 'What is the result of the expression?'
