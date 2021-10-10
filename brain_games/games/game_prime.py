"""The module contains the logic of the "Prime Number" game."""

from random import randint


def isprime(num):
    """Check if the argument is a prime number.

    Arguments:
        num: Any number.

    Returns:
        An answer whether the given number is prime or not.
    """
    if num > 1:
        for nat_num in range(2, num):
            if (num % nat_num) == 0:
                return 'no'
        return 'yes'
    return 'no'


def game_prime_logic():
    """Provide the puzzle and the answer.

    Arguments:
        No input required.

    Returns:
        A tuple containing the puzzle and the correct answer.
    """
    give_number = randint(1, 100)
    quest_num = str(give_number)
    corr_answer = isprime(give_number)

    return quest_num, corr_answer


def game_prime_rules():
    """Print the game rule to the user.

    Arguments:
        No input required.

    Returns:
        The game rule as a string.
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
