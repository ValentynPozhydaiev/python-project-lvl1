"""Module for greeting function."""
import prompt


def welcome_user():
    """Ask the user to enter his name and greet him.

    Arguments:
        No input required.

    """
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
