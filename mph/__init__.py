﻿"""Pythonic scripting interface for Comsol Multiphysics"""

# Meta information
__title__     = 'MPh'
__version__   = '0.9.1'
__date__      = '2021–03–24'
__author__    = 'John Hennig'
__copyright__ = 'John Hennig'
__license__   = 'MIT'

# Public interface
from .session import start
from .config  import option
from .client  import Client
from .server  import Server
from .model   import Model
from .node    import Node
from .java    import inspect
