import sys
import time
import datetime
import curses
import curses.ascii
from src.face import Face

class Clock:

    HELP_STR = "[H]elp [B]ar [C]olor [D]ate [F]ont [Q]uit"

    def __init__(self, config):
        self.config = config
        self.timestamp = None
        self.ignore_next_resize = False
        self.exit = False

    def start(self):
        curses.wrapper(self._start)


    def stop(self):
        curses.nocbreak()
        self.win.keypad(False)
        curses.echo()
        curses.endwin()


    def _start(self, win):
        self.win = win
        self._init_curses()
        self.config.create_colors()
        self.face = Face(self.win, self.config)

        last_second = None

        while not self.exit:
            if self.config.utc:
                self.timestamp = datetime.datetime.utcnow()
            else:
                self.timestamp = datetime.datetime.now()

            if self.timestamp.second != last_second:
                self._redraw()
                last_second = self.timestamp.second

            self._process_user_input()
            time.sleep(0.1)


    def _init_curses(self):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.win.keypad(True)
        self.win.nodelay(True)


    def _redraw(self, force_clear=False):
        if force_clear:
            self.win.clear()
        self.face.draw(self.timestamp)

        if self.config.show_help:
            self.win.addstr(0,0,Clock.HELP_STR, curses.A_STANDOUT)


    def _process_user_input(self):
        key = self.win.getch()

        if key == curses.KEY_RESIZE:
            if self.ignore_next_resize:
                self.ignore_next_resize = False
            else:
                curses.resizeterm(*self.win.getmaxyx())
                self.ignore_next_resize = True
                self._redraw(force_clear=True)

        # Why does curses not have a definitio for KEY_ESC (27) ??
        elif key in [curses.KEY_CANCEL, curses.KEY_CLOSE, curses.KEY_EXIT, 27]:
            self.exit = True

        elif key == curses.ERR or not curses.ascii.isalpha(key):
            return

        ch = chr(key)

        if ch in 'Qq':
            self.exit = True

        if ch in 'Bb':
            self.config.show_seconds_bar = not self.config.show_seconds_bar
            self._redraw(force_clear=True)

        if ch in 'Cc':
            self.config.numbers_color = self.config.get_next_color(self.config.numbers_color)
            self.config.create_colors()
            self._redraw(force_clear=True)

        if ch in 'Dd':
            self.config.show_date = not self.config.show_date
            self._redraw(force_clear=True)

        if ch in 'Ff':
            self.config.font = self.config.get_next_font(self.config.font)
            self._redraw(force_clear=True)

        if ch in 'Hh':
            self.config.show_help = not self.config.show_help
            self._redraw(force_clear=True)
