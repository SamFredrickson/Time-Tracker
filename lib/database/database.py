from database.queries import migrations
import sqlite3
import pathlib

class Database:
    path = pathlib.Path('storage').resolve()
    name = 'database.db'

    def __init__(self) -> None:
        self.__connection = sqlite3.connect(f'{self.path}/{self.name}')
        self.__cursor = self.__connection.cursor()
        self.migrate()

    def migrate(self):
        for query in migrations:
            self.__cursor.execute(query)
            self.__connection.commit()
    
    @property
    def cursor(self):
        return self.__cursor

    @property
    def connection(self):
        return self.__connection