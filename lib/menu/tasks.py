from menu.base import Menu
from menu.item import Item
from menu.actions.default import Default

class TasksMenu(Menu):
    def __init__(self, previous=None) -> None:
        self.__previous = previous
        super().__init__('Tasks', [
            Item('Add task\n', action=Default(self)),
            Item('Change task\n', action=Default(self)),
            Item('Remove task\n', action=Default(self)),
            Item('Show list\n', action=Default(self)),
            Item('Previous screen', 'red', action=Default(self.__previous))
        ])