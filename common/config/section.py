# -*- encoding: utf-8 -*-
# vim:set et tabstop=4 shiftwidth=4 nu nowrap fileencoding=utf-8:

from flask.config import ConfigAttribute


__all__ = ('ConfigSectionAttribute', )


class ConfigSubsection(object):
    def __init__(self, config):
        self.config = config


class ConfigSectionMeta(type):
    def __new__(meta, name, bases, dct):
        new_dct = {}
        config_descrs = {}

        for k, v in dct.items():
            if isinstance(v, ConfigAttribute):
                config_descrs[k] = v
            else:
                new_dct[k] = v

        if config_descrs:
            subsection_kclass = type(
                '%s__%s' % (name, ConfigSubsection.__class__.__name__),
                (ConfigSubsection, ),
                config_descrs
            )
            new_dct['subsection_class'] = subsection_kclass

        return super(ConfigSectionMeta, meta).__new__(meta, name, bases, new_dct)


class ConfigSectionAttribute(ConfigAttribute, metaclass=ConfigSectionMeta):
    def __get__(self, obj, type=None):
        rv = super(ConfigSectionAttribute, self).__get__(obj, type)
        if isinstance(rv, dict):
            return self.subsection_class(rv)
        else:
            return rv

