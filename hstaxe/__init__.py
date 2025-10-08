"""
import the toplevel functions and check the directory setup
See LICENSE.txt
"""
from importlib.metadata import version, PackageNotFoundError

from . import config
from .axesrc import axetasks
from .utils import set_logging

config.set_defaults()
config.check_axe_dirs()


try:
    __version__ = version('hstaxe')
except PackageNotFoundError:
    # package is not installed
    __version__ = 'unknown'
    __githash__ = ''
