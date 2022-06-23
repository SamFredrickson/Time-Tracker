from collections import OrderedDict
from menu.actions.action import Action
from database.models.task import Task
from database.models.taskname import TaskName
from rich.prompt import Prompt
from rich import print
from datetime import datetime

class RemoveTask(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu
        self.__task = Task()
        self.__taskname = TaskName()

    def ask(self):
        id = Prompt.ask('Task id', default=None)
        return OrderedDict([('id', id)])

    def do(self):
       data = self.ask()

       if data['id'] is None:
           self.__menu.warn('Task id is required')
           self.do()

       if self.__task.get_by_id(int(data['id'])) is None:
           self.__menu.render()
           self.__menu.warn('Task does not exist')
           item = self.__menu.ask_for_choice()
           self.__menu.call_action(item)

       self.__task.delete(int(data['id']))
       self.__menu.render()
       item = self.__menu.ask_for_choice()
       self.__menu.call_action(item)