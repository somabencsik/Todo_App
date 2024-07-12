"""Menu modul for Terminal User Interface."""

import sys

from src.model.todo_list import TodoList
from src.view.tui.add_todo import add_todo
from src.view.tui.add_todo_list import add_todo_list
from src.view.tui.utils import clear


def is_int(value: any) -> bool:
    """Checks if the given value is int or not."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def list_todos() -> None:
    """Lists every todo by todo lists."""
    for t_list in TodoList.objects:
        if len(t_list.todos) == 0:
            continue
        print(f"* {t_list.name}:")
        for todo in t_list.todos:
            print(f"\t- {todo.message}")


def menu() -> [None, add_todo, add_todo_list]:
    """Menu view for tui."""

    print("What would you like to do?")
    print("\t1. Create Todo")
    print("\t2. Create Todo List")
    print("\t3. List Todos")
    print("\tx. Exit")
    choice = input()

    if not is_int(choice) and choice.lower() == "x":
        print("\nExiting...\n")
        sys.exit()
    elif not is_int(choice):
        print("\nWrong input is given!\n")
        return

    choice = int(choice)

    if choice == 1:
        return add_todo
    elif choice == 2:
        return add_todo_list
    elif choice == 3:
        clear()
        list_todos()
        input("\nPress enter to continue...")
        return

    return
