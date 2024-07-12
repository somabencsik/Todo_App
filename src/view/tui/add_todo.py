from src.model.todo import Todo
from src.model.todo_list import TodoList


def add_todo() -> None:
    """Creates and adds Todo to a TodoList (default) if not given."""

    print("Type 'x' to cancel\n")
    message = input("Message of todo: ").strip().lower()
    todo_list_name = input("Name of todo list (optional): ").strip().lower()

    if message == "":
        print("Wrong input!")
        return add_todo
    elif message.lower() == "x":
        return

    todo = Todo(message)

    if todo_list_name == "":
        todo_list_name = "default"
    todo_list = TodoList.get_todo_list(todo_list_name)
    todo_list.add_todo(todo)
