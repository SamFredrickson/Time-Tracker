from datetime import datetime
from tracker.database import database
from database.models.model import Model

class Task(Model):
    def __init__(self) -> None:
        self.__cursor = database.cursor
        self.__connnection = database.connection
        self.__table = 'tasks'

    def get_all(self):
        self.__connnection.commit()
        query = f'''
               SELECT * FROM tasks_view
            '''
        self.__cursor.execute(query)
        self.__connnection.commit()
        tasks = self.__cursor.fetchall()
        return tasks

    def get_by_id(self, id):
        query = f'''
            SELECT * FROM {self.__table}
            WHERE id = ?
        '''
        self.__cursor.execute(query, (id, ))
        self.__connnection.commit()
        return self.__cursor.fetchone()

    def delete(self, id):
        query = f'''
            DELETE FROM {self.__table}
            WHERE id = ?
        '''
        self.__cursor.execute(query, (id, ))
        self.__connnection.commit()
        return id

    def add(
        self, 
        task_name_id: int, 
        start=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        end=None, 
        description=None
    ):
        query = f'''
                INSERT INTO {self.__table} (task_name_id, start, end, description)
                VALUES (?, ?, ?, ?) 
            '''
        self.__cursor.execute(query, (task_name_id, start, end, description))
        self.__connnection.commit()
        return self.__cursor.lastrowid

    def update(self, id, field, value):
        query = f'''
            UPDATE {self.__table} SET {field} = ? WHERE id = ?
        '''
        self.__cursor.execute(query, (value, id))
        self.__connnection.commit()