#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim:set et tabstop=4 shiftwidth=4 nu nowrap fileencoding=utf-8:

import os
import sys
import argparse
import anyjson

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(CURRENT_DIR)

from app import App


def get_cmd_arguments():
    parser = argparse.ArgumentParser(description='blumenplace-front service')
    parser.add_argument('--config', dest='config', action='store', type=str, required=True, help='configuration file')
    return parser.parse_args()


def main():
    args = get_cmd_arguments()
    app = App(os.path.abspath(args.config))
    app.run()


if __name__ == '__main__':
    main()

