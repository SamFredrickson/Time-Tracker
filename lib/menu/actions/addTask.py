from collections import OrderedDict
from menu.actions.action import Action
from database.models.task import Task
from database.models.taskname import TaskName
from rich.prompt import Prompt
from rich import print
from datetime import datetime

class AddTask(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu
        self.__task = Task()
        self.__taskname = TaskName()

    def ask(self):
        date = Prompt.ask('Date you\'d like to work with', default=datetime.now().strftime("%Y-%m-%d"))
        name = Prompt.ask('Task name', default=None)
        start = Prompt.ask('Task started', default=datetime.now().strftime("%H:%M:%S")) 
        end = Prompt.ask('Task ended', default=None)
        description = Prompt.ask('Description', default=None)
        return OrderedDict([('id', id), ('name', name), ('start', start), ('end', end), ('description', description), ('date', date)])

    def do(self):
       data = self.ask()
       start = f'{data["date"]} {data["start"]}'
       end = f'{data["date"]} {data["end"]}' if data['end'] is not None else None 

       if data['name'] is None:
           self.__menu.render()
           self.__menu.warn('Name is required')
           item = self.__menu.ask_for_choice()
           self.__menu.call_action(item)
       
       task_name_id = self.__taskname.get_or_create(data['name'])
       self.__task.add(task_name_id, start, end, data['description'])
       self.__menu.render()
       item = self.__menu.ask_for_choice()
       self.__menu.call_action(item)
