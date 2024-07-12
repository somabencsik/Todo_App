"""Module for todo list views."""

import time

from src.model.todo_list import TodoList


def add_todo_list() -> None:
    """Creates a Todo List."""
    print("Type 'x' to cancel\n")

    name = input("Name of the Todo List: ").strip().lower()
    if name.lower() == "x":
        return
    elif name == "":
        print("\nWrong input!")
        time.sleep(0.5)
        return add_todo_list
    elif TodoList.get_todo_list(name) is not None:
        print("\nThere is a todo list with the same name!")
        time.sleep(2)
        return add_todo_list

    TodoList(name)


def list_todos() -> None:
    """Lists every todo by todo lists."""
    todo_list_name = input("Name of todo list (default shows every): ").strip()
    if todo_list_name == "":
        todo_list_name = None

    print()

    for t_list in TodoList.objects:
        if todo_list_name is not None and t_list.name != todo_list_name:
            continue
        if len(t_list.todos) == 0:
            continue
        print(f"* {t_list.name}:")
        for todo in t_list.todos:
            msg = todo.message
            if todo.done:
                msg = "\u0336".join(msg) + "\u0336"
            print(f"\t- {msg}")

    input("\nPress enter to continue...")
