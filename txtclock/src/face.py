import curses
import datetime

class Face:

    def __init__(self, clock) -> None:
        self.clock = clock
        self.win = clock.win
        self.config = clock.config


    def draw(self, timestamp):
        if type(timestamp) is datetime.datetime:
            self._draw_timestamp(timestamp)
        elif type(timestamp) is str:
            self._draw_str(timestamp)
        else:
            raise Exception(f"Type of timestamp {timestamp} is unknown ({type(timestamp)})")


    def _draw_timestamp(self, timestamp):
        strlist = []
        y = 0
        font = self.config.fonts[self.config.font]

        num_lines = len(font.get('0'))
        num_cols = 0
        txt = timestamp.strftime(self.config.time_format)

        for char in txt:
            if font.char_exists(char):
                num_cols += len(font.get(char)[0])

        for line_idx in range(num_lines):
            line_str = ""
            for char in txt:
                if font.char_exists(char):
                    digit_line = font.get(char)[line_idx]
                    line_str += digit_line

            strlist.append([y, line_str])
            y += 1


        if True:
            if self.clock.timers:
                txt = ""
                for t in sorted(self.clock.timers, key=lambda t: t.remaining, reverse=True):
                    if t.elapsed_timer_mode:
                        txt += f"[{t.msg}:{t.elapsed_str}] "
                    else:
                        txt += f"[{t.msg}:{t.remaining_str}] "
            else:
                txt = " " * curses.COLS
            y += 1
            strlist.append([y, txt])
            y += 1  # Force extra separation line


        if self.config.show_date:
            txt = timestamp.strftime(self.config.date_format)
            y += 1
            strlist.append([y, txt])
            y += 1  # Force extra separation line


        if self.config.show_seconds_bar:
            bar_width = self.config.seconds_bar_size
            pos = timestamp.second / 60
            filled_width = int(pos * bar_width)
            empty_width = bar_width - filled_width
            bar_str = (self.config.second_bar_fill_char * filled_width) + (self.config.second_bar_empty_char * empty_width)
            txt = bar_str
            y += 1
            strlist.append([y, txt])

        if y > curses.LINES:
            y = 0
            start_line = 0
            strlist = [s for s in strlist if s[0]<curses.LINES]
        else:
            start_line = (curses.LINES - y) // 2

        for line in strlist:
            offset = line[0]
            txt = line[1]

            if len(txt) > curses.COLS:
                txt = txt[:curses.COLS]
            else:
                _gap = (curses.COLS - len(txt)) // 2
                _fill = " " * _gap
                txt = f"{_fill}{txt}{_fill}"

            if txt:
                self._addstr(start_line+offset, 0, txt, self.config.numbers_color_curses)


    def _draw_str(self, timestamp):
        strlist = []
        y = 0
        font = self.config.fonts[self.config.font]

        num_lines = len(font.get('0'))
        num_cols = 0
        txt = timestamp   # Timestamp already comes as string

        for char in txt:
            if font.char_exists(char):
                num_cols += len(font.get(char)[0])

        for line_idx in range(num_lines):
            line_str = ""
            for char in txt:
                if font.char_exists(char):
                    digit_line = font.get(char)[line_idx]
                    line_str += digit_line

            strlist.append([y, line_str])
            y += 1

        if y > curses.LINES:
            y = 0
            start_line = 0
            strlist = [s for s in strlist if s[0]<curses.LINES]
        else:
            start_line = (curses.LINES - y) // 2

        for line in strlist:
            offset = line[0]
            txt = line[1]

            if len(txt) > curses.COLS:
                x = 0
                txt = txt[:curses.COLS]
            else:
                x = (curses.COLS - len(txt)) // 2

            if txt:
                self._addstr(start_line+offset, x, txt, self.config.numbers_color_curses)


    def _addstr(self, *args, **kwargs):
        try:
            return self.win.addstr(*args, **kwargs)
        except Exception:
            # If curses can't show this piece of text, we'll just ignore it
            pass
