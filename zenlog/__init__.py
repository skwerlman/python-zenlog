#!/usr/bin/env python

'''

Zenlog is a logging tool for lazy people, meant for quick use of 
prettified log messages. 

It's a very light wrapper around colorlog, a wonderful library
for color output in logging messages. In addition, Zenlog hides
the standard library logger hierarchy, using only the root logging
instance.

This won't fit many advanced uses, but it's good for quick scripts
that could use easy-to-read and clear log output with a dead simple
API.

It's still missing some important things:
  * datetime support and other useful log output
  * testing on any terminal other than uxterm
  * finer-grained color control

And some not so important ones:
  * "theme" support, emulating some used log schemes (Xorg, Gentoo...)
  * Use of fancy Unicode characters
  * Additional sets of levels other than debug, info, etc?

'''
import logging
import colorlog

class Log:
    def __init__(self, lvl=logging.DEBUG, format=None):
        self._lvl = lvl
        if not format:
            self.format = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        logging.root.setLevel(self._lvl)
        self.formatter = colorlog.ColoredFormatter(self.format)
        self.stream = logging.StreamHandler()
        self.stream.setLevel(self._lvl)
        self.stream.setFormatter(self.formatter)
        self.logger = logging.getLogger('pythonConfig')
        self.logger.setLevel(self._lvl)
        self.logger.addHandler(self.stream)

    def _parse_level(lvl):
        if lvl == logging.CRITICAL or lvl in ("critical", "crit", "c", "fatal"):
            return logging.CRITICAL
        elif lvl == logging.ERROR or lvl in ("error", "err", "e"):
            return logging.ERROR
        elif lvl == logging.WARNING or lvl in ("warning", "warn", "w"):
            return logging.WARNING
        elif lvl == logging.INFO or lvl in ("info", "inf", "nfo", "i"):
            return logging.INFO
        elif lvl == logging.DEBUG or lvl in ("debug", "dbg", "d"):
            return logging.DEBUG
        else:
            raise TypeError("Unrecognized logging level: %s" % lvl)
        
    def critical(self, message, *args, **kwargs):
        self.logger.critical(message, *args, **kwargs)
    def error(self, message, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)
    def warn(self, message, *args, **kwargs):
        self.logger.warn(message, *args, **kwargs)
    warning = warn
    def info(self, message, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)
    def debug(self, message, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)

    def level(lvl=None):
        '''Get or set the logging level.'''
        if not lvl:
            return self._lvl
        self._lvl = self._parse_level(self._lvl)
        logging.root.setLevel(self._lvl)

log = Log()