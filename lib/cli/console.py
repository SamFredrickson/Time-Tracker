from typing import Optional
import typer

from tracker.release import __app_name__, __version__
from menu.main import Main

app = typer.Typer()
mainMenu = Main()

@app.command(help='Shows main menu')
def menu():
    mainMenu.render()
    item = mainMenu.ask_for_choice()
    mainMenu.call_action(item)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True
    )
) -> None:
    return