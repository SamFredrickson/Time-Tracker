from tracker.release import __version__, __author__, __app_name__
from cli.console import app
from database.database import Database

database = Database()

def main():
    app(prog_name=__app_name__)

main()