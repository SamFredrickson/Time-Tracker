from datetime import datetime
from typing import Optional
from utils.date import get_year_pattern
import typer
from menu.actions.showTasks import ShowTasks

from tracker.release import __app_name__, __version__
from menu.main import Main
from menu.tasks import TasksMenu
from menu.actions.showTasks import ShowTasks
from menu.actions.view_task import ViewTask
from menu.actions.delete_task import DeleteTask
from menu.actions.add_task import AddTask

app = typer.Typer()

@app.command(help='Shows main menu')
def menu():
    mainMenu = Main()
    mainMenu.render()
    item = mainMenu.ask_for_choice()
    mainMenu.call_action(item)

@app.command(help='Shows tasks list')
def task_list(
    date_from=typer.Option(datetime.now().strftime(get_year_pattern()), help="Date from, default today"), 
    date_to=typer.Option(datetime.now().strftime(get_year_pattern()), help="Date to, default today"), 
):
    main_menu = Main()
    tasks_menu = TasksMenu(main_menu)
    show_tasks = ShowTasks(tasks_menu)
    show_tasks.cli_do(date_from, date_to)

@app.command(help='View task info')
def task_view(id: int = typer.Option(None, help="Task id")):    
     main_menu = Main()
     view_task = ViewTask(menu=main_menu, previous=main_menu)  
     view_task.cli_do(id)

@app.command(help='Delete task')
def task_delete(id: int = typer.Option(None, help="Task id")):
     main_menu = Main()
     delete_action = DeleteTask(main_menu)
     delete_action.cli_do(id)

@app.command(help='Create task')
def task_create():
     main_menu = Main()
     delete_action = AddTask(main_menu)
     delete_action.do()

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