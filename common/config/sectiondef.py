# -*- encoding: utf-8 -*-
# vim:set et tabstop=4 shiftwidth=4 nu nowrap fileencoding=utf-8:

import os

from flask.config import ConfigAttribute

from common.config.section import ConfigSectionAttribute


class CryptoConfigAttribute(ConfigSectionAttribute):
    private = ConfigAttribute('private', get_converter=os.path.abspath)

    public = ConfigAttribute('public', get_converter=os.path.abspath)

    def __init__(self):
        super(CryptoConfigAttribute, self).__init__('crypto')

