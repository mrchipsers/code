
"""mastermind package

This package re-exports the implementation in :mod:`mastermind.mastermind`
so that tests (and other code) can simply do ``import mastermind`` and
access the functions defined in ``mastermind.py``.
"""

from .mastermind import *  # re-export functions for top-level import

__all__ = [name for name in dir() if not name.startswith("_")]
