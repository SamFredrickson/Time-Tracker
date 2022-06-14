from tracker.database import database
from database.models.model import Model

class Task(Model):
    def __init__(self) -> None:
        self.__cursor = database.cursor
        self.__connnection = database.connection
        self.__name = 'tasks'

    def add(
        self, 
        name: str, 
        start: str, 
        end=None, 
        description=None
    ):
        query = f'''
            INSERT INTO {self.__name} (name, start, end, description)
            VALUES (?, ?, ?, ?) 
        '''
        self.__cursor.execute(query)
