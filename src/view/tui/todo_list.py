"""Module for todo list views."""

import time

from src.model.todo_list import TodoList
from src.view.tui.utils import check_choice, print_menu


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


def list_todos(edit_mode: bool = False, todo_list_name: str = "") -> None:
    """Lists every todo by todo lists."""
    if todo_list_name == "":
        todo_list_name = input("Name of todo list (default shows every): ").strip()
    if todo_list_name == "":
        todo_list_name = None

    print()

    todos = {}
    offset = 0
    for list_idx, t_list in enumerate(TodoList.objects):
        if todo_list_name is not None and t_list.name != todo_list_name:
            continue
        list_number = list_idx + offset + 1
        print(f"* {f'{list_number}.' if edit_mode else ''} {t_list.name}:", end="")
        todos[list_number] = {}
        offset += list_idx + 1

        if len(t_list.todos) == 0:
            print(" No todos\n")
            continue

        print()

        for todo_idx, todo in enumerate(t_list.todos):
            msg = todo.message
            if todo.done:
                msg = "".join(["\u0336{}".format(c) for c in msg])
            todo_number = offset + todo_idx + 1
            print(f"\t- {f'{todo_number}.' if edit_mode else ''} {msg}")
            todos[list_number][todo_number] = todo
        offset += todo_idx

    # TODO: Clean up/refactor edit mode!!!
    if edit_mode:
        print("\nPossibilities:")
        menu_points = {
            1: ("Swtich status", lambda todo: todo.change_status()),
            "x": ("Cancel", list_todos),
        }
        print_menu(menu_points)
        choice = input("\nInput ([list number] [todo number] [menu point]): ")
        if choice == "x":
            return menu_points[choice][1]
        list_num, todo_num, choice = choice.split()
        list_num, todo_num, choice = int(list_num), int(todo_num), int(choice)
        menu_points[choice][1](todos[list_num][todo_num])
        return lambda: list_todos(True, todo_list_name)

    menu_points = {
        1: ("Edit todo(s)", lambda: list_todos(True, todo_list_name)),
        "x": ("Go back", ...),
    }

    print("\nWhat would you like to do?\n")
    print_menu(menu_points)
    choice = input("\nInput: ")

    res = check_choice(choice, menu_points)
    if not res:
        return
    choice = int(choice)

    return menu_points[choice][1]
