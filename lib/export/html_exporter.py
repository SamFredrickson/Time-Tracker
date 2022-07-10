from typing import List
from utils.date import get_difference, get_formatted_total
from .exporter import Exporter
from datetime import datetime
from database.types.task import Task as TaskType
import pathlib

class HtmlExporter(Exporter):
    format = 'html'
    root_path = pathlib.Path('lib', 'export', 'templates').resolve()

    def __init__(self) -> None:
        super().__init__()

    def write(self, tasks=List[TaskType]):
        content_concatinated = ''

        with open(self.content_path, 'r') as file:
            content = file.read()
        with open(self.template_path, 'r') as file:
            template = file.read()
        
        total_days = 0
        total_hours = 0
        total_minutes = 0
        total_seconds = 0

        for task in tasks:
            difference = get_difference(task.start, task.end)
            total_days += difference['days']
            total_hours += difference['hours']
            total_minutes += difference['minutes']
            total_seconds += difference['seconds']

            content_concatinated += content.format(
                id=task.id,
                name=task.name,
                start=task.start,
                end=task.end,
                total=task.difference,
                description=task.description
            )

        content_concatinated += content.format(
                id='—',
                name='—',
                start='—',
                end='—',
                total=get_formatted_total(total_days, total_hours, total_minutes, total_seconds),
                description='—'
            )
        
        name = self.generate_name()
        template_formatted = template.format(
            content=content_concatinated,
        )

        with open(f'{self.path}/{name}', 'wt') as file:
            file.write(template_formatted)

    @property
    def content_path(self):
        return f'{self.root_path}/content.html'

    @property
    def template_path(self):
        return f'{self.root_path}/template.html'