from menu.base import Menu
from menu.item import Item
from menu.actions.default import Default
from menu.actions.tasks import Tasks
from menu.actions.exit import Exit
from menu.actions.settings import Settings


class Main(Menu):
    def __init__(self) -> None:
        super().__init__('Main Menu', [
            Item('Tasks\n', action=Tasks(self)),
            # Item('Tracking settings\n', action=Settings(self)),
            Item('Exit', 'red', action=Exit())
        ])