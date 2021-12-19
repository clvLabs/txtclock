from src.fonts import FontBase

class Font(FontBase):

    def __init__(self, off_char="·", on_char="■") -> None:
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
            "| ",
            "| ",
            "| ",
            "| ",
            "| ",
            "| ",
            "| ",
            "| ",
            "| ",
        ],
        "/" : [
            "/ ",
            "/ ",
            "/ ",
            "/ ",
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
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
        ],
        "1" : [
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "O ",
        ],
        "2" : [
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "O ",
            "O ",
        ],
        "3" : [
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "O ",
            "O ",
            "O ",
        ],
        "4" : [
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "O ",
            "O ",
            "O ",
            "O ",
        ],
        "5" : [
            "Z ",
            "Z ",
            "Z ",
            "Z ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
        ],
        "6" : [
            "Z ",
            "Z ",
            "Z ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
        ],
        "7" : [
            "Z ",
            "Z ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
        ],
        "8" : [
            "Z ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
        ],
        "9" : [
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
            "O ",
        ],
    }
