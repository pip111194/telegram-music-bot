"""
Handlers Module
Imports all command handlers for the music bot
"""

# Import all handler modules
from . import music
from . import admin
from . import misc
from . import platforms
from . import free_platforms

__all__ = ['music', 'admin', 'misc', 'platforms', 'free_platforms']
