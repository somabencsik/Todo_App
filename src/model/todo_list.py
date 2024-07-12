"""This module contains the information for TodoList model."""

from __future__ import annotations

from src.model.todo import Todo


class TodoList:
    """
    Class description for TodoList model.

    Attributes
    ----------
    """

    objects: list[TodoList] = []

    def __init__(self, name: str) -> None:
        self.name = name

        self.todos: list[Todo] = []

        TodoList.objects.append(self)

    def add_todo(self, todo: Todo) -> bool:
        """
        Checks if the given todo is correct and adds to the list.

        Parameters
        ----------
        todo : Todo
            The Todo you want to add to the list
        """
        if not isinstance(todo, Todo):
            return False

        self.todos.append(todo)
        return True

    @staticmethod
    def get_todo_list(name: str) -> [None, TodoList]:
        """Returns the TodoLists by name."""
        for t_list in TodoList.objects:
            if t_list.name != name:
                continue
            return t_list
