import argparse
from .config import Config

class Args:

    @staticmethod
    def _parse_bool(value):
        value = str(value)
        retval = value.upper() in ["TRUE", "1", "YES", "Y"]
        return retval

    @staticmethod
    def read():
        parser = argparse.ArgumentParser()

        parser.add_argument('--write_config', type=str, help='write config file an exit', default=None)
        parser.add_argument('--config_file', type=str, help='set config file to use', default=None)

        for name in Config._defaults:
            default = Config._defaults[name]
            value = default['value']
            help = default.get("help", "")
            shorthand = default.get("shorthand", None)

            _type = type(value)
            if _type is bool:
                _type = Args._parse_bool

            if shorthand:
                parser.add_argument(f'-{shorthand}', f'--{name}', help=help, type=_type, default=None)
            else:
                parser.add_argument(f'--{name}', help=help, type=_type, default=None)

        return parser.parse_args()
