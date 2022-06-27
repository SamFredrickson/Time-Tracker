from menu.actions.action import Action
from rich.prompt import Prompt
from rich import print
from datetime import datetime
from rich.console import Console
from menu.tables.task import TaskTable
from database.types.date_range import DateRange

class PaginationMode(Action):
    def __init__(self, menu, date_paginator, task, previous) -> None:
        self.__menu = menu
        self.__date_paginator = date_paginator
        self.__task = task
        self.__previous = previous
        self.__console = Console()

    def get_table_by_date(self, date: str):
        date_range = DateRange(date, date)
        tasks = self.__task.get_tasks(date_range=date_range)
        title = f'[b][yellow]{date_range.date_range_formatted}[/b]'
        task_table = TaskTable(title=title, tasks=tasks)
        return {
            'tasks': tasks,
            'table': task_table.table
        }

    def do(self):
        print('[b][yellow]Tip: use the words below to change tasks by date or exit to exit[/b]')
        data = None
        
        while True:
            word = Prompt.ask("Word", default='next', choices=['next', 'prev', 'curr', 'exit'])
            
            if word == 'next':
                data = self.get_table_by_date(self.__date_paginator.next)
                self.__console.print(data['table'])

            if word == 'prev':
                data = self.get_table_by_date(self.__date_paginator.prev)
                self.__console.print(data['table'])

            if word == 'curr':
                data = self.get_table_by_date(self.__date_paginator.curr)
                self.__console.print(data['table'])

            if word == 'exit':
                if data is None:
                    self.__previous.render()
                    choice = self.__previous.ask_for_choice()
                    self.__previous.call_action(choice)
                    break

                if data is not None:
                   if data['tasks']:
                        template = self.__menu.get_template()
                        print(template)
                        choice = self.__menu.ask_for_choice()
                        self.__menu.call_action(choice)
                        break

                   if not data['tasks']:
                         self.__previous.render()
                         choice = self.__previous.ask_for_choice()
                         self.__previous.call_action(choice)
                         break
                break
            