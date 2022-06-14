from tracker.database import database
from database.models.model import Model

class TaskName(Model):
    def __init__(self) -> None:
        self.__cursor = database.cursor
        self.__connnection = database.connection
        self.__name = 'tasks_names'

    def getByName(self, name):
        self.__cursor.execute(f'SELECT * FROM {self.__name} WHERE name = "{name}"')
        self.__connnection.commit()
        data = self.__cursor.fetchall()
        return data

    def getAll(self):
        self.__cursor.execute('select * from tasks_names')
        self.__connnection.commit()
        rows = self.__cursor.fetchall()
        print(rows)

    def add(self, name):
        query = f'''
            INSERT INTO {self.__name} (name)
            VALUES (?)
        '''
        self.__connnection.commit()
        return self.__cursor.execute(query, (name, ))