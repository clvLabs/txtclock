from src.fonts import FontBase

class Font(FontBase):

    def __init__(self, off_char="0", on_char="1") -> None:
        super().__init__()
        self.off_char = off_char
        self.on_char = on_char


    def get(self, char):
        if char in self._digits:
            return [line.replace('Z', self.off_char).replace('O', self.on_char) for line in self._digits[char]]
        else:
            return char


    _digits = {
        ":" : [
            ": ",
            ": ",
            ": ",
            ": ",
            ": ",
        ],
        "/" : [
            "/ ",
            "/ ",
            "/ ",
            "/ ",
            "/ ",
        ],
        "0" : [
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "0 ",
        ],
        "1" : [
            "Z ",
            "Z ",
            "Z ",
            "O ",
            "1 ",
        ],
        "2" : [
            "Z ",
            "Z ",
            "O ",
            "Z ",
            "2 ",
        ],
        "3" : [
            "Z ",
            "Z ",
            "O ",
            "O ",
            "3 ",
        ],
        "4" : [
            "Z ",
            "O ",
            "Z ",
            "Z ",
            "4 ",
        ],
        "5" : [
            "Z ",
            "O ",
            "Z ",
            "O ",
            "5 ",
        ],
        "6" : [
            "Z ",
            "O ",
            "O ",
            "Z ",
            "6 ",
        ],
        "7" : [
            "Z ",
            "O ",
            "O ",
            "O ",
            "7 ",
        ],
        "8" : [
            "O ",
            "Z ",
            "Z ",
            "Z ",
            "8 ",
        ],
        "9" : [
            "O ",
            "Z ",
            "Z ",
            "O ",
            "9 ",
        ],
    }
