import curses

class Face:

    name = "default"
    description = "Default txtclock face"
    author = "Tony Aguilar"

    def __init__(self, win, config) -> None:
        self.win = win
        self.config = config


    def draw(self, timestamp):
        try:
            self._draw(timestamp)
        except:
            pass    # !!!!


    def _draw(self, timestamp):
        strlist = []
        y = 0
        txt = timestamp.strftime(self.config.time_format)
        strlist.append([y, txt])
        y += 1

        if self.config.show_date:
            txt = timestamp.strftime(self.config.date_format)
            y += 1
            strlist.append([y, txt])
            y += 1

        if self.config.show_seconds_bar:
            bar_width = self.config.seconds_bar_size
            pos = timestamp.second / 60
            filled_width = int(pos * bar_width)
            empty_width = bar_width - filled_width
            bar_str = (self.config.second_bar_fill_char * filled_width) + (self.config.second_bar_empty_char * empty_width)
            txt = bar_str
            y += 1
            strlist.append([y, txt])
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
                self.win.addstr(start_line+offset, x, txt)
