from typing import List
from rich.table import Table
from rich.text import Text
from rich import box
from rich import print
from rich.panel import Panel
from database.types.task import Task
from utils.date import get_difference
from rich.console import Console


class TaskTable:
    def __init__(self, title: Text, tasks: List[Task]) -> None:
        self.__table = Table(title=title, expand=True, box=box.ROUNDED)
        self.__table.add_column("S. No.", style="cyan", no_wrap=True)
        self.__table.add_column("Task name", style="white")
        self.__table.add_column("Total", justify="right")

        self.__total_days = 0
        self.__total_hours = 0
        self.__total_minutes = 0
        self.__total_seconds = 0

        for task in tasks:
            difference = get_difference(task.start, task.end)
            self.__total_days += difference['days']
            self.__total_hours += difference['hours']
            self.__total_minutes += difference['minutes']
            self.__total_seconds += difference['seconds']

            self.__table.add_row(
                str(task.id), 
                task.name, 
                f'[b][grey24]{task.difference}[/b]'
            )

        self.__table.add_row(
            '——',
            '——', 
            self.total,
            style='on black',
            end_section=True
        )

    @property            
    def table(self):
        return self.__table

    @property
    def total(self):
        return f'[b][red]{self.__total_days}d {self.__total_hours}h {self.__total_minutes}m {self.__total_seconds}s[/b]'