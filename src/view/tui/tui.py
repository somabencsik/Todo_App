"""Terminal User Interface view modul for Todo App."""

from src.model.todo_list import TodoList
from src.view.tui.menu import menu
from src.view.tui.utils import clear


def setup() -> None:
    """Creates default values."""
    TodoList("default")


def start():
    """Starts the Terminal User Interface."""
    setup()

    is_running = True

    current_view = menu

    while is_running:
        clear()
        res = current_view()

        if res is None:
            current_view = menu
            continue

        current_view = res
