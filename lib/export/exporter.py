import pathlib
from datetime import datetime

class Exporter:
    folder_name = 'export'
    format = 'csv'
    path = pathlib.Path(folder_name).resolve()

    def __init__(self) -> None:
        if not pathlib.Path(self.path).is_dir():
            pathlib.Path(self.path).mkdir()
    
    def generate_name(self):
        '''generate name for future file in export folder'''
        date = datetime.now().strftime( "%Y_%m_%d" )
        time = datetime.now().strftime( "%H_%M_%S" )
        return f'export_{date}_{time}.{self.format}'