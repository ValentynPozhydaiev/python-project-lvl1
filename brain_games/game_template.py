"""The template for all games."""

from prompt import string


def game_template(usr_name, game_rule, game_logic):
    """Initiate the game of guessing the even/odd nature of numbers.

    Arguments:
        usr_name: The user name obtained after call of welcome_user().
        game_logic: game rules which will be printed to the user.
        game_rule: the function which defines the game and returns the condition
        as well as the correct answer to compare the user input with.
    """
    number_guesses = 0
    print(game_rule())
    while number_guesses < 3:
        game_quest, corr_answer = game_logic()
        print('Question: {0}'.format(game_quest))
        user_answer = string('Your answer: ')
        if user_answer == corr_answer:
            print('Correct!')
            number_guesses += 1
        else:
            announce_message = '{0} is wrong answer ;(. Correct answer was {1}.'
            print(announce_message.format(user_answer, corr_answer))
            print("Let's try again, {0}!".format(usr_name))
            break
    if number_guesses == 3:
        print('Congratulations, {0}!'.format(usr_name))
