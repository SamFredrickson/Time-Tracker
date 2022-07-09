from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from tracker.release import __version__, __author__, __app_name__
from cli.console import app

app(prog_name=__app_name__)