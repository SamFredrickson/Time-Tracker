from typing import Optional
import typer
from menu.actions.showTasks import ShowTasks

from tracker.release import __app_name__, __version__
from menu.main import Main
from menu.tasks import TasksMenu
from menu.actions.showTasks import ShowTasks
from menu.actions.view_task import ViewTask

app = typer.Typer()

@app.command(help='Shows main menu')
def menu():
    mainMenu = Main()
    mainMenu.render()
    item = mainMenu.ask_for_choice()
    mainMenu.call_action(item)

@app.command(help='Shows tasks list')
def task_list():
    main_menu = Main()
    tasks_menu = TasksMenu(main_menu)
    show_tasks = ShowTasks(tasks_menu)
    show_tasks.do()

@app.command(help='View task info')
def task_view():
     main_menu = Main()
     view_task = ViewTask(menu=main_menu)  
     view_task.do()

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