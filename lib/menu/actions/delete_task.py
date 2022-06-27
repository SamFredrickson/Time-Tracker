from menu.actions.action import Action

class DeleteTask(Action):
    def __init__(self, menu, previous=None) -> None:
        self.__menu = menu
        self.__name = "delete"

    # def do(self, id: int):
    #     self.__task.delete(id)

    @property
    def name(self):
        return self.__name