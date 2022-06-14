class Item():
    def __init__(
            self, 
            name: str, 
            color='white',
            action=None
        ) -> None:
        self.__name = name
        self.__color = color
        self.__action = action

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def action(self):
        return self.__action