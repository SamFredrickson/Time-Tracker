from collections import OrderedDict
from typing import List
from menu.view_menu import ViewMenu
from menu.actions.action import Action
from database.types.task import Task as TaskType
from database.types.task_view import TaskViewType
from database.models.task import Task
from rich import print
from rich.console import Console
from rich.prompt import Prompt

class ViewTask(Action):
    def __init__(self, menu, previous=None) -> None:
        self.__menu = menu
        self.__view_menu = ViewMenu(previous=self.__menu)
        self.__task = Task()
        self.__previous = previous
        self.__console = Console()

    def get_formatted_list(self, task: TaskType):
        return TaskViewType(task.id, task.name, task.start, task.end, task.description, task.date_created).get_props()

    def do(self):
        id = Prompt.ask("Task number", default='1')
        task = self.__task.get_by_id(id)
        if not task:
            self.__menu.warn("Task does not exist")
            return self.do()
        
        for item in self.get_formatted_list(task):
            print(item)

        view_menu = self.__view_menu.get_template()
        print(view_menu)
        item = self.__view_menu.ask_for_choice()

        if hasattr(item.action, 'name'):
             if item.action.name == 'delete':
                self.__task.delete(id)
                self.__previous.render()
                item = self.__previous.ask_for_choice()
                self.__previous.call_action(item)
                return True

        self.__view_menu.call_action(item)