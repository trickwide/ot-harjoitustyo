from tkinter import Tk
from src.ui.user_interface import UI


def main():
    window = Tk()
    window.title("Budget Tracker")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
