import sys

from src.view.tui.tui import start as tui


def start_gui():
    """Starts the gui view."""
    print("Not implemented.")


def start_tui():
    """Starts the tui view."""
    tui()


if __name__ == "__main__":
    _, args = sys.argv

    starter = "tui"
    if len(args) != 0 and "gui" in args:
        starter = "gui"

    if starter == "tui":
        start_tui()
        exit()

    start_gui()
