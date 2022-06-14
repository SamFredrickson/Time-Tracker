from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from menu.decorators import clear_screen

class Menu():
    def __init__(self, title: str, items: list) -> None:
        self.__title = title
        self.__items = items

    @clear_screen
    def render(self):
        template = ''
        for index, item in self.items:
            name = item.name
            color = item.color
            template += f"{index} - [{color}]{name}[/{color}]"
        panel = Panel(template, title=f"[yellow]{self.__title}")
        print(panel)

    def ask_for_choice(self):
        choice = Prompt.ask(
            'Your choice',
            choices=[str(index) for index, item in self.items],
        )
        items = dict(self.items)
        return items[int(choice)]

    def call_action(self, item):
        item.action.do()

    @property
    def title(self):
        return self.__title
    
    @property
    def items(self):
        return enumerate(self.__items, 1)