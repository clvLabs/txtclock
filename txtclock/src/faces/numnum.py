import curses

class Face:

    name = "numnum"
    description = "Numbers made of Numbers !"
    author = "Tony Aguilar"

    digits = {
        ":" : [
            "      ",
            "      ",
            "      ",
            "  ##  ",
            "  ##  ",
            "      ",
            "      ",
            "      ",
            "      ",
            "      ",
            "  ##  ",
            "  ##  ",
            "      ",
            "      ",
        ],
        "0" : [
            "   0000000      ",
            "  0000000000    ",
            " 0000    0000   ",
            "000        000  ",
            "000        000  ",
            "000        000  ",
            "000        000  ",
            "000        000  ",
            "000        000  ",
            "000        000  ",
            "0000      0000  ",
            " 0000    0000   ",
            "  0000000000    ",
            "    000000      ",
        ],
        "1" : [
            "    11111       ",
            "  1111111       ",
            "  111 111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
            "      111       ",
        ],
        "2" : [
            "  22222222      ",
            " 22222222222    ",
            " 22      2222   ",
            "          222   ",
            "          222   ",
            "         2222   ",
            "         222    ",
            "       2222     ",
            "      2222      ",
            "    22222       ",
            "   2222         ",
            " 2222           ",
            "2222222222222   ",
            "2222222222222   ",
        ],
        "3" : [
            " 333333333      ",
            " 33333333333    ",
            " 33      333    ",
            "         3333   ",
            "         333    ",
            "   33333333     ",
            "   3333333      ",
            "      333333    ",
            "         3333   ",
            "          333   ",
            "          333   ",
            " 33      3333   ",
            "333333333333    ",
            " 333333333      ",
        ],
        "4" : [
            "         4444   ",
            "        44444   ",
            "       444444   ",
            "      444 444   ",
            "     444  444   ",
            "    444   444   ",
            "   444    444   ",
            "  444     444   ",
            " 44444444444444 ",
            "444444444444444 ",
            "          444   ",
            "          444   ",
            "          444   ",
            "          444   ",
        ],
        "5" : [
            "   5555555555   ",
            "  55555555555   ",
            " 555            ",
            " 555            ",
            " 55             ",
            " 555555555      ",
            " 55555555555    ",
            "         5555   ",
            "          555   ",
            "          555   ",
            "          555   ",
            " 5      5555    ",
            "55555555555     ",
            " 55555555       ",
        ],
        "6" : [
            "      6666666   ",
            "    666666666   ",
            "   66666        ",
            "  666           ",
            " 666            ",
            " 66666666666    ",
            "66666666666666  ",
            "6666       666  ",
            "666        6666 ",
            "666        6666 ",
            " 666       666  ",
            " 6666     6666  ",
            "  66666666666   ",
            "    6666666     ",
        ],
        "7" : [
            "7777777777777   ",
            "7777777777777   ",
            "         7777   ",
            "         777    ",
            "        777     ",
            "       777      ",
            "      7777      ",
            "     7777       ",
            "    7777        ",
            "    777         ",
            "   7777         ",
            "  7777          ",
            " 7777           ",
            " 777            ",
        ],
        "8" : [
            "     88888888   ",
            "  88888888888   ",
            " 8888     8888  ",
            " 888       888  ",
            " 8888     8888  ",
            " 88888  88888   ",
            "    8888888     ",
            "  88888888888   ",
            " 8888     8888  ",
            "8888       8888 ",
            "8888       8888 ",
            " 8888     8888  ",
            "  88888888888   ",
            "    8888888     ",
        ],
        "9" : [
            "     9999999    ",
            "  99999999999   ",
            " 9999     9999  ",
            " 999       999  ",
            "9999       999  ",
            "9999       999  ",
            " 9999     9999  ",
            "  999999999999  ",
            "   9999999 999  ",
            "          9999  ",
            "         9999   ",
            "       99999    ",
            "  99999999      ",
            "  999999        ",
        ],
    }

    small_digits = {
        "0" : [ "0 " ],
        "1" : [ "1 " ],
        "2" : [ "2 " ],
        "3" : [ "3 " ],
        "4" : [ "4 " ],
        "5" : [ "5 " ],
        "6" : [ "6 " ],
        "7" : [ "7 " ],
        "8" : [ "8 " ],
        "9" : [ "9 " ],
    }


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

        num_lines = len(Face.digits['0'])
        num_cols = 0
        txt = timestamp.strftime(self.config.time_format)

        for char in txt:
            if char in Face.digits:
                num_cols += len(Face.digits[char][0])

        for line_idx in range(num_lines):
            line_str = ""
            for char in txt:
                if char in Face.digits:
                    digit_line = Face.digits[char][line_idx]
                    line_str += digit_line

            strlist.append([y, line_str])
            y += 1


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
                x = 0
                txt = txt[:curses.COLS]
            else:
                x = (curses.COLS - len(txt)) // 2

            if txt:
                self.win.addstr(start_line+offset, x, txt)
