from datetime import datetime
from tracker.database import database
from database.models.model import Model
from database.types.date_range import DateRange
from database.types.task import Task as TaskType

class Task(Model):
    def __init__(self) -> None:
        self.__cursor = database.cursor
        self.__connnection = database.connection
        self.__table = 'tasks'

    def get_tasks(self, date_range: DateRange):
        task_list = []
        self.__connnection.commit()
        query = f'''
               SELECT * FROM tasks 
               WHERE date_created >= ?
               AND date_created <= ?
            '''
        self.__cursor.execute(query, (date_range.date_from, date_range.date_to))
        self.__connnection.commit()
        tasks = self.__cursor.fetchall()
        for task in tasks:
            id, name, start, end, description, date_created = task
            task_list.append(TaskType(id=id, name=name, start=start, end=end, description=description, date_created=date_created))
        return task_list

    def get_by_id(self, id):
        query = f'''
            SELECT * FROM {self.__table}
            WHERE id = ?
        '''
        self.__cursor.execute(query, (id, ))
        self.__connnection.commit()
        task = self.__cursor.fetchone()
        if not task:
            return task
        id, name, start, end, description, date_created = task
        return TaskType(id=id, name=name, start=start, end=end, description=description, date_created=date_created)

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