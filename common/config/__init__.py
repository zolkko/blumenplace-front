# -*- encoding: utf-8 -*-
# vim:set et tabstop=4 shiftwidth=4 nu nowrap fileencoding=utf-8:

import os

from flask.config import Config as BaseConfig
from yaml import load as load_yaml


__all__ = ('ConfigError', 'Config')


class ConfigError(Exception):
    def __init__(self, message):
        super(ConfigError, self).__init__()
        self.message = message

    def __repr__(self):
        return '<%s("%s")>' % (ConfigError.__class__.__name__, self.message)


class Config(BaseConfig):
    """Overrides behaviour of the Flask.Config dictionary."""

    def __init__(self, yaml_file, root_path, defaults=None):
        super(Config, self).__init__(root_path, defaults)

        if not os.path.exists(yaml_file):
            raise ConfigError('Configuration file "%s" does not exists.' % yaml_file)

        with open(yaml_file, 'r') as f:
            conf_data = f.read()

        self.update(load_yaml(conf_data))

