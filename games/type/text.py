import curses
import random


class Text:
    def __init__(self, stdscr, file_name) -> None:
        self.stdscr = stdscr
        self.file_name = file_name
        self.target = self.load_text(file_name)
        self.current_text = []
        self.wpm = 0

    def display_text(self):
        self.stdscr.addstr(self.target)
        self.stdscr.addstr(1, 0, f"WPM: {self.wpm}")

        for i, char in enumerate(self.current_text):
            correct_char = self.target[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            self.stdscr.addstr(0, i, char, color)

    def load_text(self, filename):
        with open(filename, "r") as quoates:
            lines = quoates.readlines()
            return random.choice(lines).strip()

    def initialize_state(self):
        self.target_text = self.load_text(self.file_name)
        self.current_text = []
        self.wpm = 0
        self.stdscr.nodelay(True)

    def update_wpm(self, wpm):
        self.wpm = wpm

    def get_wpm(self):
        return self.wpm

    def get_current_text(self):
        return self.current_text

    def get_target_text(self):
        return self.target

    def get_stdscr(self):
        return self.stdscr

    def clear(self):
        self.stdscr.clear()

    def refresh(self):
        self.stdscr.refresh()

    def is_complete(self):
        return "".join(self.current_text) == self.target

    def delete_text(self):
        self.current_text.pop()

    def add_text(self, text):
        self.current_text.append(text)

