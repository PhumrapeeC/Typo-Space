import curses
import random


class Text:
    def __init__(self, stdscr, file_name) -> None:
        self.__stdscr = stdscr
        self.__file_name = file_name
        self.__target = self.load_text(file_name)
        self.__current_text = []
        self.__wpm = 0

    def display_text(self):
        self.__stdscr.addstr(self.__target)
        self.__stdscr.addstr(1, 0, f"WPM: {self.__wpm}")

        for i, char in enumerate(self.__current_text):
            correct_char = self.__target[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            self.__stdscr.addstr(0, i, char, color)

    def load_text(self, filename):
        with open(filename, "r") as quoates:
            lines = quoates.readlines()
            return random.choice(lines).strip()

    def initialize_state(self):
        self.target_text = self.load_text(self.__file_name)
        self.__current_text = []
        self.__wpm = 0
        self.__stdscr.nodelay(True)

    def update_wpm(self, wpm):
        self.__wpm = wpm

    def get_wpm(self):
        return self.__wpm

    def get_current_text(self):
        return self.__current_text

    def get_target_text(self):
        return self.__target

    def get_stdscr(self):
        return self.__stdscr

    def clear(self):
        self.__stdscr.clear()

    def refresh(self):
        self.__stdscr.refresh()

    def is_complete(self):
        return "".join(self.__current_text) == self.__target

    def delete_text(self):
        self.__current_text.pop()

    def add_text(self, text):
        self.__current_text.append(text)

