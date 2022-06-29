from menu.actions.default import Default
from menu.base import Menu
from menu.item import Item
from menu.actions.delete_task import DeleteTask
from menu.actions.update_task import UpdateTask

class ViewMenu(Menu):
    def __init__(self, previous=None) -> None:
        self.__previous = previous
        super().__init__('View Task Options', [
            Item('Delete\n', action=DeleteTask(self)),
            Item('Update\n', action=UpdateTask(self.__previous)),
            Item('Exit', 'red', action=Default(self.__previous)),
        ])