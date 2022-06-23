from menu.base import Menu
from menu.item import Item
from menu.actions.default import Default

class SettingsMenu(Menu):
    def __init__(self, previous=None) -> None:
        self.__previous = previous
        super().__init__('Tracking settings', [
            Item('New day beginning time\n', action=Default(self)),
            Item('Previous screen', 'red', action=Default(self.__previous)),
        ])