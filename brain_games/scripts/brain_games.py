#!/usr/bin/env python3

"""The module contains the main executable script."""

from brain_games.cli import welcome_user


def greet():
    """Display the greeting phrase.

    Arguments:
        No input required.
    """
    print('Welcome to the Brain Games!')


def main():
    """Run the main script.

    Arguments:
        No input required.
    """
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
