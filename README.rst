*******
BOND
*******

BOND is a simple time tracker console application. It handles tasks creation,
editing, deleliton, showing and exporting.

Design Principles
=================

*  Have an extremely simple setup process with a minimal learning curve.
*  Create some tasks with their name, description, optionally start time and finish time
*  Watch them by manipulating simple menu or cli
*  Update, Delete, Finish, Continue or Filter by date
*  Export

Installation
=================

git clone https://github.com/SamFredrickson/Time-Tracker time_tracker
cd time_tracker

python -m venv venv (optionally)
source venv/bin/activate (optionally)

python setup.py install

Usage
=================

The console application allows you to manipulate tasks in two ways:
1. Menu (``tracker menu``)
2. Console commands (``tracker [command] [arguments]``)

Use ``tracker menu`` to show availiable commands
Use ``tracker [command] --help`` to show help for specfic console command

Authors
=======

BOND was created by `Sam Fredrickson <https://github.com/samFredrickson/>`