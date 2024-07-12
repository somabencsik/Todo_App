import time

from src.model.todo_list import TodoList


def add_todo_list() -> None:
    """Creates a Todo List."""
    print("Type 'x' to cancel\n")

    name = input("Name of the Todo List: ").strip().lower()
    if name.lower() == "x":
        return
    elif name == "":
        print("Wrong input!")
        time.sleep(0.5)
        return add_todo_list

    TodoList(name)
