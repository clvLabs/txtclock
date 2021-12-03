import os
import sys
import configparser

class Config:

    appname = "txtclock"

    filename = f"{appname}.conf"

    _defaults = {
        "twenty_four_h":    { "value": True,            "help": "use 24h mode?",         "shorthand": "24" },
        "show_date":        { "value": False,           "help": "show date?",            "shorthand": "d" },
        "show_seconds_bar": { "value": False,           "help": "show seconds bar?",     "shorthand": "b" },
        "font":             { "value": "default",       "help": "font style" },
        "time_format":      { "value": "%H:%M:%S",      "help": "time format" },
        "date_format":      { "value": "%Y/%m/%d",      "help": "date format" },
        "numbers_color":    { "value": "38;5;10",       "help": "color for numbers" },
        "separators_color": { "value": "38;5;240",      "help": "color for separators" },
    }

    _locations = [
        os.curdir,
        os.path.expanduser("~"),
        os.path.expanduser(f"~/.config/{appname}"),
        f"/etc/{appname}",
        os.environ.get(f"{appname.upper()}_CONF"),
    ]


    def __init__(self):
        from .args import Args
        args = Args.read()

        for name in Config._defaults:
            if getattr(args, name, None) is not None:
                setattr(self, name, getattr(args, name))
            else:
                setattr(self, name, Config._defaults[name]['value'])

        setattr(self, "args", args)

        parser = configparser.ConfigParser()
        _config_files = [f"{path}/{Config.filename}" for path in Config._locations]
        parser.read(_config_files)

        if Config.appname in parser:
            for prop in Config._defaults:
                if getattr(args, prop, None) is None:
                    if prop in parser[Config.appname]:
                        setattr(self, prop, parser[Config.appname][prop])


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
