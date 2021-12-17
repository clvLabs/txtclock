#!/usr/bin/python3
# coding=utf-8

import sys
from src.config import config
from src.clock import Clock

if config.args.write_config:
    config.write(config.args.write_config)
    print(f"Configuration file written to {config.args.write_config}/{config.filename}")
    sys.exit(0)

clock = Clock(config)

try:
    clock.start()
except KeyboardInterrupt:
    clock.stop()

sys.exit(0)
