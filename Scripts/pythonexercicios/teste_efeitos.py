import time
import curses

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        stdscr.clear()
        stdscr.addstr(10, 10, "Bem-vindo ao meu programa Python!", curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.5)
        stdscr.clear()
        stdscr.refresh()
        time.sleep(0.5)

if __name__ == "__main__":
    curses.wrapper(main)