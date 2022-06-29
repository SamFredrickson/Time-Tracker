from menu.actions.action import Action
from database.models.task import Task
from rich.prompt import Confirm
from rich import print

class DeleteTask(Action):
    def __init__(self, menu) -> None:
        self.__menu = menu
        self.__task = Task()
        self.__name = "delete"

    # def do(self, id: int):
    #     self.__task.delete(id)

    def cli_do(self, id: int):
        task = self.__task.get_by_id(id)
        if task is None:
            self.__menu.warn('Task does not exist')
            return False
        print(f'[b]Task: [red]{task.id} - {task.name}[/b]')
        sure = Confirm.ask('Are you sure?')
        if sure:
            self.__task.delete(id)
            self.__menu.success('Task successfully deleted')

    @property
    def name(self):
        return self.__name