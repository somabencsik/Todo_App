import time

from src.model.todo import Todo
from src.model.todo_list import TodoList


def add_todo() -> None:
    """Creates and adds Todo to a TodoList (default) if not given."""

    print("Type 'x' to cancel\n")
    message = input("Message of todo: ").strip().lower()
    if message.lower() == "x":
        return
    elif message == "":
        print("Wrong input!")
        time.sleep(0.5)
        return add_todo

    todo_list_name = input("Name of todo list (optional): ").strip().lower()

    todo = Todo(message)

    if todo_list_name == "":
        todo_list_name = "default"
    todo_list = TodoList.get_todo_list(todo_list_name)
    todo_list.add_todo(todo)
