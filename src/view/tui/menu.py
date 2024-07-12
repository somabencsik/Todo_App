"""Menu modul for Terminal User Interface."""

import sys
import time

from src.view.tui.add_todo import add_todo
from src.view.tui.todo_list import add_todo_list, list_todos
from src.view.tui.utils import check_choice, print_menu


def menu() -> [None, add_todo, add_todo_list]:
    """Menu view for tui."""

    menu_points = {
        1: ("Create Todo", add_todo),
        2: ("Create Todo List", add_todo_list),
        3: ("List Todos", list_todos),
        "x": ("Exit", sys.exit),
    }

    print("What would you like to do?\n")
    print_menu(menu_points)
    choice = input("\nInput: ")

    res = check_choice(choice, menu_points)
    if not res:
        if choice.lower() == "x":
            print("\nExiting... Have a nice day!\n")
            time.sleep(1)
            return sys.exit
        print("\nWrong input is given!\n")
        time.sleep(1)
        return

    choice = int(choice)
    return menu_points[choice][1]
