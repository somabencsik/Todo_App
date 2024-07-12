"""Menu modul for Terminal User Interface."""

import sys
import time

from src.view.tui.add_todo import add_todo
from src.view.tui.todo_list import add_todo_list, list_todos


def is_int(value: any) -> bool:
    """Checks if the given value is int or not."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def menu() -> [None, add_todo, add_todo_list]:
    """Menu view for tui."""

    menu_points = {
        1: ("Create Todo", add_todo),
        2: ("Create Todo List", add_todo_list),
        3: ("List Todos", list_todos),
        "x": ("Exit", sys.exit),
    }

    print("What would you like to do?\n")
    for key, value in menu_points.items():
        print(f"\t{key}. {value[0]}")
    choice = input("\nInput: ")

    if not is_int(choice) and choice.lower() == "x":
        print("\nExiting... Have a nice day!\n")
        time.sleep(1)
        return sys.exit
    elif not is_int(choice):
        print("\nWrong input is given!\n")
        time.sleep(1)
        return

    choice = int(choice)
    if choice not in menu_points:
        print("\nWrong input is given!\n")
        time.sleep(1)
        return

    return menu_points[choice][1]
