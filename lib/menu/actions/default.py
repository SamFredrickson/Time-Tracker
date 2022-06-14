from menu.actions.action import Action

class Default(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu

    def do(self):
        self.__menu.render()
        item = self.__menu.ask_for_choice()
        self.__menu.call_action(item)
