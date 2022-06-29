from collections import OrderedDict
from wsgiref import validate
from menu.actions.action import Action
from database.models.task import Task
from rich.prompt import Prompt
from rich import print
from datetime import datetime
from utils.date import get_time_pattern, get_year_pattern, validate_date_pattern

class AddTask(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu
        self.__task = Task()

    def ask_and_validate(self):
        date = Prompt.ask('Date', default=datetime.now().strftime( get_year_pattern() ))
        name = Prompt.ask('Task name', default=None)
        start = Prompt.ask('Task started', default=datetime.now().strftime( get_time_pattern() )) 
        end = Prompt.ask('Task ended', default=None)
        description = Prompt.ask('Description', default=None)

        validated_date = validate_date_pattern(date)
        validated_start = validate_date_pattern(start, r'\d\d:\d\d:\d\d')

        if validated_date is False:
            self.__menu.warn('Invalid Date format. Example: 2022-02-02')
            return self.ask_and_validate()

        if validated_start is False:
            self.__menu.warn('Invalid Start format. Example: 00:30:00')
            return self.ask_and_validate()

        if end is not None:
            if validate_date_pattern(end, r'\d\d:\d\d:\d\d') is False:
                self.__menu.warn('Invalid End format. Example: 00:32:00')
                return self.ask_and_validate()
            end = f'{date} {end}'
        
        if name is None:
            self.__menu.warn('Name is required')
            return self.ask_and_validate()
        
        if self.__task.is_task_exists_for_date(date, name) is not None:
            self.__menu.warn(f'This task name is exists for this date ({date})')
            return self.ask_and_validate()
        
        start = f'{date} {start}'

        return OrderedDict([('name', name), ('start', start), ('end', end), ('description', description), ('date', date)])

    def do(self):
       data = self.ask_and_validate()

       self.__task.add(data['name'], data['start'], data['end'], data['description'])
       self.__menu.render()
       item = self.__menu.ask_for_choice()
       self.__menu.call_action(item)