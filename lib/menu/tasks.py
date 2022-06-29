from menu.base import Menu
from menu.item import Item
from menu.actions.default import Default
from menu.actions.add_task import AddTask
from menu.actions.showTasks import ShowTasks
from menu.actions.removeTask import RemoveTask
from menu.actions.changeTask import ChangeTask

class TasksMenu(Menu):
    def __init__(self, previous=None) -> None:
        self.__previous = previous
        super().__init__('Tasks', [
            Item('Add task\n', action=AddTask(self)),
            Item('Show list\n', action=ShowTasks(self)),
            Item('Previous screen', 'red', action=Default(self.__previous))
        ])