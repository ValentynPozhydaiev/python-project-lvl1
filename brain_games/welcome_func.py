"""This module contains greeting functions."""

from prompt import string


def greet():
    """Display the greeting phrase.

    Arguments:
        No input required.
    """
    print('Welcome to the Brain Games!')


def welcome_user():
    """Ask the user to enter his name and greet him.

    Arguments:
        No input required.

    Returns:
        The user name.
    """
    user_name = string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
    return user_name
