from menu.base import Menu
from menu.item import Item
from menu.actions.delete_task import DeleteTask
from menu.actions.default import Default

class ViewMenu(Menu):
    def __init__(self, previous=None) -> None:
        self.__previous = previous
        super().__init__('View Task Options', [
            Item('Delete\n', action=DeleteTask(self)),
            Item('Update\n', action=Default(self.__previous)),
            Item('Finish\n', action=Default(self.__previous)),
            Item('Continue\n', action=Default(self.__previous)),
            Item('Previous screen', 'red', action=Default(self.__previous)),
        ])