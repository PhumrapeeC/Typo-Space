import curses
from curses import wrapper
import time
from games.type.text import Text

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    result_wpm = 0
    text = Text(stdscr, "data/word.txt")
    start_time = time.time()
    text.initialize_state()
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(text.get_current_text()) / (time_elapsed / 60)) / 5)
        text.update_wpm(wpm)
        text.clear()
        text.display_text()
        text.refresh()

        if text.is_complete():
            text.get_stdscr().nodelay(False)
            result_wpm = text.get_wpm()
            break

        try:
            key = text.get_stdscr().getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(text.get_current_text()) > 0:
                text.delete_text()
        elif len(text.get_current_text()) < len(text.get_target_text()):
            text.add_text(key)  

    return result_wpm

def play():
    return wrapper(main)
