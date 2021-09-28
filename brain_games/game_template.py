"""The template for all games."""

from random import randint

from prompt import string


def guess_even_number(usr_inp):
    """Initiate the game of guessing the even/odd nature of numbers.

    Arguments:
        usr_inp: The user name obtained after call of welcome_user().

    """
    number_guesses = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while number_guesses < 3:
        give_number = randint(1, 100)
        print('Question: {0}'.format(give_number))
        user_answer = string('Your answer: ')
        corr_answer = 'yes' if give_number % 2 == 0 else 'no'
        if user_answer == corr_answer:
            print('Correct!')
            number_guesses += 1
        else:
            announce_message = '{0} is wrong answer ;(. Correct answer was {1}.'
            print(announce_message.format(user_answer, corr_answer))
            print("Let's try again, {0}!".format(usr_inp))
            break
    if number_guesses == 3:
        print('Congratulations, {0}!'.format(usr_inp))
