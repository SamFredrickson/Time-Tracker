from utils.date import get_formatted_difference
from rich.text import Text

class Task:
    def __init__(
        self, 
        id: int, 
        name: str, 
        start: str, 
        date_created: str, 
        description=None, 
        end=None
    ) -> None:
        self.__id = id
        self.__name = name
        self.__start = start
        self.__date_created = date_created
        self.__description = description
        self.__end = end

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def start(self):
        return self.__start

    @property
    def date_created(self):
        return self.__date_created

    @property
    def description(self):
        return self.__description

    @property
    def end(self):
        return self.__end

    @property
    def difference(self):
        return get_formatted_difference(self.__start, self.__end)