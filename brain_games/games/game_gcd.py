"""The module contains the logic of the "Greater Common Diviser" game."""

from math import gcd
from random import randint


def game_gcd_logic():
    """Provide the puzzle and the answer.

    Arguments:
        No input required.

    Returns:
        A tuple containing the puzzle and the correct answer.
    """
    first_rand = randint(1, 200)
    second_rand = randint(1, 200)
    question = '{0} {1}'.format(first_rand, second_rand)
    corr_answer = str(gcd(first_rand, second_rand))

    return question, corr_answer


def game_gcd_rules():
    """Print the game rule to the user.

    Arguments:
        No input required.

    Returns:
        The game rule as a string.
    """
    return 'Find the greatest common divisor of given numbers.'
