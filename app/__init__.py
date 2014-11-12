# -*- encoding: utf-8 -*-
# vim:set et tabstop=4 shiftwidth=4 nu nowrap fileencoding=utf-8:

from flask import Flask
from flask.config import ConfigAttribute

from common.config import Config
from common.config.sectiondef import CryptoConfigAttribute


class App(Flask):
    """Rather than passing arguments to run method this implementation
    uses configuration file to define HOST:PORT variables.
    """

    #: This host name or IP address to listen.
    host = ConfigAttribute('host')

    #: Port number to listen.
    port = ConfigAttribute('port')

    #: Cryptography section.
    crypto = CryptoConfigAttribute()

    def __init__(self, json_config_path):
        self.json_config_path = json_config_path
        super(App, self).__init__(__name__)

    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return Config(self.json_config_path, root_path, self.default_config)

    def run(self, **options):
        super(App, self).run(self.host, self.port, self.debug, **options)

