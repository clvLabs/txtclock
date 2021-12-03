#!/usr/bin/python3
# coding=utf-8

import sys
from src.config import config

if config.args.write_config:
    config.write(config.args.write_config)
    print(f"Configuration file written to {config.args.write_config}/{config.filename}")
    sys.exit(0)

print(config)
