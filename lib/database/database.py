import sqlite3
from database.queries import create_tables_queries

class Database:
    name = 'database.db'
    def __init__(self) -> None:
        self.__connection = sqlite3.connect(self.name)
        self.__cursor = self.__connection.cursor()
        self.__create_tables()

    def __create_tables(self):
        for query in create_tables_queries:
            self.__cursor.execute(query)
            self.__connection.commit()
    
    @property
    def cursor(self):
        return self.__cursor

    @property
    def connection(self):
        return self.__connection