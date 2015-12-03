# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:35:20 2015

@author: steve
"""
from collections import OrderedDict
from ConfigParser import ConfigParser as _ConfigParser


class ConfigParser(_ConfigParser):

    # modified to accept file names as input
    def write(self, fp):
        """Write an .ini-format representation of the configuration state."""
        if isinstance(fp, file):
            _ConfigParser.write(self, fp)
        elif isinstance(fp, basestring):
            with open(fp, 'wb') as fpp:
                _ConfigParser.write(self, fpp)
        else:
            raise TypeError('fp must be of type file or basestring')

    def to_dict(self):
        """Export ConfigParser Object to OrderedDict"""
        d = OrderedDict.fromkeys(self.sections())
        for section in d.keys():
            d[section] = dict(self.items(section))
        return d

    @staticmethod
    def from_dict(d):
        """Import Dict to create new ConfigParser Object"""
        c = ConfigParser()
        for section in d.keys():
            c.add_section(section)
            for option, value in d[section].iteritems():
                c.set(section, option, value)
        return c
