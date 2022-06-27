from collections import OrderedDict
from menu.actions.action import Action
from database.models.task import Task
from menu.tables.task import TaskTable
from database.types.date_range import DateRange
from utils.date import DatePaginator
from utils.date import validate_date_pattern, get_year_pattern
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich import print
from datetime import datetime
from menu.tasks_table_menu import TasksTableMenu

class ShowTasks(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu
        self.__console = Console()
        self.__task = Task()

    def get_validated_data(self):
        default = datetime.now().strftime(get_year_pattern())
        date_from = Prompt.ask("Choose date from", default=default)
        date_to = Prompt.ask("Choose date to", default=default)
        
        validated_from = validate_date_pattern(date_from)
        validated_to = validate_date_pattern(date_to)

        if validated_from is False or validated_to is False:
            self.__menu.warn('Invalid date format. Example: 2022-02-02')
            return self.get_validated_data()

        return OrderedDict([('date_from', date_from), ('date_to', date_to)])

    def do(self):
        data = self.get_validated_data()
        date_range = DateRange(data['date_from'], data['date_to'])
        tasks = self.__task.get_tasks(date_range=date_range)
        title = f'[b][yellow]{date_range.date_range_formatted}[/b]'
        task_table = TaskTable(title=title, tasks=tasks)
        self.__console.clear()
        
        tasks_not_empty = True if tasks else False
        self.__task_table_menu = TasksTableMenu(
            date_paginator=DatePaginator(date_range.date_from),
            previous=self.__menu, 
            tasks_not_empty=tasks_not_empty,
            task=self.__task
        )

        self.__console.print(task_table.table)
        print(self.__task_table_menu.get_template())
        choice = self.__task_table_menu.ask_for_choice()
        self.__task_table_menu.call_action(choice)

        # self.__console.print('[b][yellow]Tip: Use (next, prev, curr) word to change date[/b]')

        # while True:
        #      word = Prompt.ask("Word", default='next', choices=['next', 'prev', 'curr', 'exit'])
        #      print(word)