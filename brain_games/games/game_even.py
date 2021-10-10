"""The module contains the logic of the "Guess the Even Number" game."""

from random import randint


def game_even_logic():
    """Provide the puzzle and the answer.

    Arguments:
        No input required.

    Returns:
        A tuple containing the puzzle and the correct answer.
    """
    give_number = randint(1, 100)
    corr_answer = 'yes' if give_number % 2 == 0 else 'no'
    quest_num = str(give_number)

    return quest_num, corr_answer


def game_even_rules():
    """Print the game rule to the user.

    Arguments:
        No input required.

    Returns:
        The game rule as a string.
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'
