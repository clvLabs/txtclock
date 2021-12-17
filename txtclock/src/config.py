import os
import sys
import configparser

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
                        default_val = Config._defaults[prop]['value']

                        if type(default_val) is bool:
                            setattr(self, prop, parser.getboolean(Config.appname, prop))
                        elif type(default_val) is int:
                            setattr(self, prop, parser.getint(Config.appname, prop))
                        elif type(default_val) is float:
                            setattr(self, prop, parser.getfloat(Config.appname, prop))
                        else:
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
