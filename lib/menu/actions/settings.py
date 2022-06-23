from menu.actions.action import Action
from menu.settings import SettingsMenu

class Settings(Action):
    def __init__(self, previous=None) -> None:
        self.__menu = SettingsMenu(previous=previous)

    def do(self):
        self.__menu.render()
        item = self.__menu.ask_for_choice()
        self.__menu.call_action(item)