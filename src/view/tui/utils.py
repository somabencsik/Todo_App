"""Modul for functions that are used in multiple scripts."""

import os


def clear() -> None:
    """Clears the terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
