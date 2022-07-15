from database.queries import migrations
import sqlite3
import os

class Database:
    def __init__(self) -> None:
        home = os.path.join(os.path.expanduser('~'), '.local', 'share')
        database_dir = os.path.join(home, 'tracker')
        name = 'bond.db'

        if not os.path.exists(database_dir):
            os.makedirs(database_dir, 0o744)

        db_path = os.path.join(database_dir, name)

        self.__connection = sqlite3.connect(db_path)
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