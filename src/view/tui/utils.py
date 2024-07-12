"""Modul for functions that are used in multiple scripts."""

import os


def clear() -> None:
    """Clears the terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def is_int(value: any) -> bool:
    """Checks if the given value is int or not."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_choice(choice: any, options: dict) -> bool:
    """Checks the choice if it is correct."""
    if not is_int(choice):
        return False

    choice = int(choice)
    if choice not in options:
        return False

    return True


def print_menu(menu: dict) -> None:
    """Print out a menu nicely."""
    for key, value in menu.items():
        print(f"\t{key}. {value[0]}")
