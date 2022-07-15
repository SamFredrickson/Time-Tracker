import os
from datetime import datetime

class Exporter:
    folder_name = 'export'
    format = 'csv'
    home = os.path.join(os.path.expanduser('~'), '.local', 'share')
    export_dir = os.path.join(home, 'tracker', 'export')

    def __init__(self) -> None:
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir, 0o744)

    def generate_name(self):
        '''generate name for future file in export folder'''
        date = datetime.now().strftime( "%Y_%m_%d" )
        time = datetime.now().strftime( "%H_%M_%S" )
        return f'export_{date}_{time}.{self.format}'