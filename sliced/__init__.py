"""
    sliced
    ======

    A simple Python slicing toolkit.

    :copyright: (c) 2014 by Brian Peterson.
    :license: Apache 2.0, see LICENSE for more details.
"""
import sliced
from ._compat import *
from .core import as_list, slice_, slices, cut
from .endpoint import EndPoint
from .exceptions import OptionNotFound, InvalidSliceString
from .headers import Headers
from .grammar import Grammar
from .interval import Interval

__all__ = [
    'slices', 'slice_', 'cut',
    'EndPoint', 'Interval', 'Grammar',
    'EndPointValueError', 'ZeroEndPointNotAllowed', 'OriginValueError',
    'InvalidIntervalType', 'InvalidStepSize', 'InvalidSliceString',
    'InvalidSeparator', 'UnknownDialect'
]

__version__ = '0.5'
