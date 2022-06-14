from menu.actions.action import Action
from menu.tasks import TasksMenu

class AddTask(Action):
    def __init__(self) -> None:
        self.__menu = TasksMenu()

    def do(self):
        self.__menu.render()
        item = self.__menu.ask_for_choice()
        self.__menu.call_action(item)