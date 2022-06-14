from menu.actions.action import Action

class MainAction(Action):
    def __init__(self) -> None:
        self.__menu = 'assa'

    def do(self):
        self.__menu.render()
        item = self.__menu.ask_for_choice()
        self.__menu.call_action(item)