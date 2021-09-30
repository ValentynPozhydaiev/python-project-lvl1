"""The module contains the logic of the "Arithmetic Progression" game."""

from random import randint


def gen_seq():
    """Generate the arithmetic progression.

    Arguments:
        No input required.

    Returns:
        A list of numbers in arithmetic progression.
    """
    first_rand = randint(1, 100)
    second_rand = randint(first_rand, 100)
    step = randint(1, 10)
    return list(range(first_rand, second_rand, step))


def game_progression_logic():
    """Provide the puzzle and the answer.

    Arguments:
        No input required.

    Returns:
        A tuple containing the puzzle and the correct answer.
    """
    sequence = gen_seq()

    if 4 < len(sequence) < 11:
        rand_index = randint(0, len(sequence) - 1)
        corr_answer = str(sequence[rand_index])
        sequence[rand_index] = '..'
        final_sequence = ' '.join(map(str, sequence))
        return final_sequence, corr_answer
    return game_progression_logic()


def game_progression_rules():
    """Print the game rule to the user.

    Arguments:
        No input required.

    Returns:
        The game rule as a string.
    """
    return 'What number is missing in the progression?'
