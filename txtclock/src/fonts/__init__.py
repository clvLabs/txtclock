import sys
import importlib
import pathlib

def get(font_name):

    module_name = f"src.fonts.{font_name}"

    try:
        tmp_module = __import__(module_name, fromlist=[''])
        importlib.reload(tmp_module)

        try:
            return tmp_module.Font
        except AttributeError:
            # print(f"EXCEPTION: {sys.exc_info()}")
            return None

    except:
        # print(f"EXCEPTION: {sys.exc_info()}")
        return None


class FontBase:

    _digits = {}


    def get(self, char):
        if char in self._digits:
            return self._digits[char]
        else:
            return char


    def char_exists(self, char):
        return char in self._digits

