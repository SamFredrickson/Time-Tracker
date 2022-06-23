from tracker.database import database
from database.models.model import Model

class TaskName(Model):
    def __init__(self) -> None:
        self.__cursor = database.cursor
        self.__connnection = database.connection
        self.__table = 'tasks_names'

    def get_by_name(self, name):
        query = f'SELECT * FROM {self.__table} WHERE name = ?'
        self.__cursor.execute(query, (name, ))
        self.__connnection.commit()
        data = self.__cursor.fetchone()
        return data

    def get_by_id(self, id):
        query = f'''
            SELECT * FROM {self.__table}
            WHERE id = ?
        '''
        self.__cursor.execute(query, (id, ))
        self.__connnection.commit()
        return self.__cursor.fetchone()

    def get_or_create(self, name):
        data = self.get_by_name(name)
        if data is not None:
            return data[0]
        return self.add(name)

    def delete(self, id):
        query = f'''
            DELETE FROM {self.__table}
            WHERE id = ?
        '''
        self.__cursor.execute(query, (id, ))
        self.__connnection.commit()
        return id
        

    def get_all(self):
        self.__cursor.execute(f'SELECT * FROM {self.__table}')
        self.__connnection.commit()
        rows = self.__cursor.fetchall()
        return rows

    def add(self, name):
        query = f'''
            INSERT INTO {self.__table} (name)
            VALUES (?)
        '''
        self.__cursor.execute(query, (name, ))
        self.__connnection.commit()
        return self.__cursor.lastrowid
    
    def update(self, id, name):
        query = f'''
            UPDATE {self.__table} SET name = ? WHERE id = ?
        '''
        self.__cursor.execute(query, (name, id))
        self.__connnection.commit()