import time
import datetime
import subprocess
import curses
import curses.ascii
from src.face import Face
from src.timer import Timer

class Clock:

    HELP_STR = "[h]elp [b]ar [cC]olor [d]ate [fF]ont [tT]imer [q]uit"

    def __init__(self, config):
        self.config = config
        self.timestamp = None
        self.ignore_next_resize = False
        self.exit = False
        self.timers = []

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
        self._main_loop()


    def _init_curses(self):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.win.keypad(True)
        self.win.nodelay(True)


    def _main_loop(self):
        last_second = None

        while not self.exit:
            if self.config.utc:
                self.timestamp = datetime.datetime.utcnow()
            else:
                self.timestamp = datetime.datetime.now()

            if self.timestamp.second != last_second:
                self._redraw()
                last_second = self.timestamp.second

            if any([t.elapsed for t in self.timers]):
                for t in self.timers:
                    if t.elapsed:
                        time_str = time.strftime("%H:%M:%S", time.localtime(t.start_time))
                        msg = f"{t.duration_str} timer started at {time_str} FINISHED"
                        if t.msg:
                            msg += f"\n{t.msg}"

                        self._show_notification(msg)

                self.timers = [t for t in self.timers if not t.elapsed]

            self._process_user_input()
            time.sleep(0.1)


    def _show_notification(self, msg):
        msg = f"[txtclock]\n{msg}"
        subprocess.Popen(["notify-send", "-u", "Critical", f"{msg}"])


    def _redraw(self, force_clear=False):
        if force_clear:
            self.win.clear()
        self.face.draw(self.timestamp)

        if self.config.show_help:
            self.win.addstr(0, 0, Clock.HELP_STR, curses.A_STANDOUT)


    def _get_user_time_display_str(self, user_str):
        s = f"{user_str:>6}".replace(' ', '0')
        return f"{s[:2]}:{s[2:4]}:{s[4:6]}"


    def _input_user_time(self, msg):
        self.win.clear()
        user_str = ""
        self.win.addstr(0, 0, msg, curses.A_STANDOUT)
        exit = False
        while not exit:
            self.face.draw(self._get_user_time_display_str(user_str))
            self.win.nodelay(False)
            c = self.win.getch()
            self.win.nodelay(True)

            if c == curses.KEY_CANCEL or c == 27:
                user_str = ""
                exit = True
            elif c == curses.KEY_ENTER or c == 10:
                exit = True
            elif c == curses.KEY_BACKSPACE:
                user_str = user_str[:-1]
            elif c >= ord('0') and c <= ord('9'):
                if len(user_str) == 6:
                    continue

                if len(user_str) == 0 and c == ord('0'):
                    continue

                user_str += chr(c)

        self._redraw(force_clear=True)
        return self._get_user_time_display_str(user_str)


    def _input_user_string(self, msg):
        self.win.clear()
        user_str = ""
        self.win.addstr(0, 0, msg, curses.A_STANDOUT)
        exit = False
        while not exit:
            self.win.addstr(1, 0, user_str)
            self.win.nodelay(False)
            c = self.win.getch()
            self.win.nodelay(True)

            if c == curses.KEY_CANCEL or c == 27:
                user_str = ""
                exit = True
            elif c == curses.KEY_ENTER or c == 10:
                exit = True
            elif c == curses.KEY_BACKSPACE:
                user_str = user_str[:-1]
                self.win.addstr(1, 0, user_str+" ")
            else:
                user_str += chr(c)

        self._redraw(force_clear=True)
        return user_str


    def _set_timer(self):
        timer_str = self._input_user_time("Enter timeout:")
        if not timer_str:
            return

        hours = int(timer_str[:2])
        minutes = int(timer_str[3:5])
        seconds = int(timer_str[6:8])

        seconds += hours * 3600
        seconds += minutes * 60

        msg = self._input_user_string("Enter message (leave blank for default message):")
        self.timers.append(Timer(seconds, msg))


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

        if ch in 'c':
            self.config.numbers_color = self.config.get_next_color(self.config.numbers_color)
            self.config.create_colors()
            self._redraw(force_clear=True)

        if ch in 'C':
            self.config.numbers_color = self.config.get_prev_color(self.config.numbers_color)
            self.config.create_colors()
            self._redraw(force_clear=True)

        if ch in 'Dd':
            self.config.show_date = not self.config.show_date
            self._redraw(force_clear=True)

        if ch in 'f':
            self.config.font = self.config.get_next_font(self.config.font)
            self._redraw(force_clear=True)

        if ch in 'F':
            self.config.font = self.config.get_prev_font(self.config.font)
            self._redraw(force_clear=True)

        if ch in 'Hh':
            self.config.show_help = not self.config.show_help
            self._redraw(force_clear=True)

        if ch in 'Tt':
            self.config.show_help = False
            self._set_timer()
