from typing import List
from menu.base import Menu
from menu.item import Item
from menu.actions.default import Default
from menu.actions.pagination_mode import PaginationMode
from menu.actions.view_task import ViewTask
from database.types.task import Task as TaskType
from utils.date import DatePaginator

class TasksTableMenu(Menu):
    def __init__(
        self, 
        date_paginator: DatePaginator, 
        task=None,
        previous=None, 
        tasks_not_empty=True,
    ) -> None:

        self.__previous = previous
        self.__menu_items = [
            Item('View task\n', action=ViewTask(self, previous=previous)),
            Item('Pagination mode\n', action=PaginationMode(self, date_paginator=date_paginator, task=task, previous=self.__previous)),
            Item('Previous screen', 'red', action=Default(self.__previous))
        ]

        super().__init__('Tasks Options', self.__menu_items)