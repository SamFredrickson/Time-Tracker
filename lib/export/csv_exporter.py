from typing import Dict, List
from .exporter import Exporter
from datetime import datetime
import csv

class CsvExporter(Exporter):
    def __init__(self) -> None:
        super().__init__()

    def write(self, fieldnames=List[str], data=Dict):
        name = self.generate_name()
        with open(f'{self.path}/{name}', 'wt') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)