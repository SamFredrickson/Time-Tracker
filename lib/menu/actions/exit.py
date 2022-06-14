from menu.actions.action import Action
from menu.decorators import clear_screen 

class Exit(Action):
    @clear_screen
    def do(self):
        quit()
