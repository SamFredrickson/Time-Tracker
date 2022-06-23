from menu.actions.action import Action
from database.models.task import Task
from database.models.taskname import TaskName
from utils.date import get_formatted_difference
from rich.prompt import Prompt
from rich import print
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box

class ShowTasks(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu
        self.__task = Task()

    def do(self):
       title = Text(f'Tasks ({datetime.now().strftime("%Y-%m-%d")})')
       title.stylize('bold blue')
       table = Table(title=title, expand=True, box=box.ROUNDED)
       table.add_column("S. No.", style="cyan", no_wrap=True)
       table.add_column("Task name", style="white")
       table.add_column("Total", justify="right")
       for item in self.__task.get_all():
           id, name, start, end, desc, date_created = item

           formatted = get_formatted_difference(start, end)
           total = Text(formatted)
           total.stylize('green')
              
           name = Text(name)
           name.stylize('grey74')

           table.add_row(str(id), name, total)

       console = Console()
       console.print(table)
