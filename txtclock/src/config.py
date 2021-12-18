import os
import sys
import configparser
import curses

class Config:

    appname = "txtclock"

    filename = f"{appname}.conf"

    _defaults = {
        "utc":                   { "value": False,           "help": "use UTC instead of local time?" },
        "face":                  { "value": "default",       "help": "select clock face",     "shorthand": "f" },
        "show_date":             { "value": False,           "help": "show date?",            "shorthand": "d" },
        "show_seconds_bar":      { "value": False,           "help": "show seconds bar?",     "shorthand": "b" },
        "seconds_bar_size":      { "value": 60,              "help": "seconds bar size" },
        "second_bar_fill_char":  { "value": "░",             "help": "fill char for seconds bar"},
        "second_bar_empty_char": { "value": "·",             "help": "fill char for seconds bar"},
        "show_help":             { "value": False,           "help": "show help bar?"},
        "time_format":           { "value": "%H:%M:%S",      "help": "time format" },
        "date_format":           { "value": "%Y/%m/%d",      "help": "date format" },
        "numbers_color":         { "value": "green",         "help": "color for numbers", "is_color": True },
    }

    _locations = [
        os.curdir,
        os.path.expanduser("~"),
        os.path.expanduser(f"~/.config/{appname}"),
        f"/etc/{appname}",
        os.environ.get(f"{appname.upper()}_CONF"),
    ]

    colors = {
        "black": curses.COLOR_BLACK,
        "blue": curses.COLOR_BLUE,
        "cyan": curses.COLOR_CYAN,
        "green": curses.COLOR_GREEN,
        "magenta": curses.COLOR_MAGENTA,
        "red": curses.COLOR_RED,
        "white": curses.COLOR_WHITE,
        "yellow": curses.COLOR_YELLOW,
    }


    def __init__(self):
        self._last_color_id = 0

        from .args import Args
        args = Args.read()

        for name in Config._defaults:
            if getattr(args, name, None) is not None:
                value = getattr(args, name)
            else:
                value = Config._defaults[name]['value']

            setattr(self, name, value)

        setattr(self, "args", args)

        parser = configparser.ConfigParser()
        _config_files = [f"{path}/{Config.filename}" for path in Config._locations]
        parser.read(_config_files)

        if Config.appname in parser:
            for prop in Config._defaults:
                if getattr(args, prop, None) is None:
                    if prop in parser[Config.appname]:
                        default_val = Config._defaults[prop]['value']

                        if type(default_val) is bool:
                            setattr(self, prop, parser.getboolean(Config.appname, prop))
                        elif type(default_val) is int:
                            setattr(self, prop, parser.getint(Config.appname, prop))
                        elif type(default_val) is float:
                            setattr(self, prop, parser.getfloat(Config.appname, prop))
                        else:
                            setattr(self, prop, parser[Config.appname][prop])


    def get_next_color(self, color):
        color_keys = list(Config.colors.keys())
        current_index = color_keys.index(color)
        current_index += 1
        if current_index >= len(color_keys):
            current_index = 0
        if color_keys[current_index] == 'black':    # Skip black
            current_index += 1
        return color_keys[current_index]


    def create_colors(self):
        for prop in Config._defaults:
            value = getattr(self, prop)
            is_color = Config._defaults[prop].get("is_color", False)
            if is_color:
                setattr(self, f"{prop}_curses", self._create_color(value))


    def _create_color(self, colorstr):
        parts = colorstr.replace(" ","").split(",")
        fg = parts[0]
        bg = parts[1] if len(parts)>1 else "black"
        self._last_color_id += 1
        curses.init_pair(self._last_color_id, self.colors[fg], self.colors[bg])
        color_id = self._last_color_id
        return curses.color_pair(color_id)


    def __str__(self) -> str:
        retval = f"{Config.appname} config: \n"
        for prop in Config._defaults:
            retval += f"- {prop}: {getattr(self, prop)}\n"
        return retval


    def __repr__(self) -> str:
        retval = f"<{self.__class__} "
        for prop in Config._defaults:
            retval += f"{prop}: {getattr(self, prop)}, "
        retval = retval[:-2]
        retval += f">"
        return retval


    def write(self, path) -> str:
        if not os.path.isdir(path):
            print(f"ERROR: {path} is not a valid folder, cant' write config file")
            sys.exit(1)

        parser = configparser.RawConfigParser()
        parser.add_section(Config.appname)
        for prop in Config._defaults:
            value = str(getattr(self, prop))

            # Fix for % chars  :)
            if '%' in value:
                value = value.replace('%', '%%')

            parser.set(Config.appname, prop, value)

        _fullpath = f"{path}/{Config.filename}"

        try:
            with open (_fullpath, "w") as f:
                parser.write(f)
            return True
        except:
            print(sys.exc_info())
            return False


config = Config()
