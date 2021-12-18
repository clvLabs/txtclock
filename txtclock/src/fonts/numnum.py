import src.fonts

class Font(src.fonts.FontBase):

    def __init__(self) -> None:
        super().__init__()
        bb = src.fonts.get("bigblocks")("X")

        digit_list = ":/0123456789"
        self._digits = { char: [line.replace('X', char) for line in bb.get(char)] for char in digit_list }
