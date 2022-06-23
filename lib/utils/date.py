from datetime import datetime
from time import time
from settings.settings import JsonSettings

json_settings = JsonSettings()

def get_current_date_range():
    return {
        'from': datetime.now().strftime("%Y-%m-%d 00:00:00"),
        'to': datetime.now().strftime("%Y-%m-%d 23:59:59")
    }

def get_formatted_difference(start: datetime, end: None):
     date_start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
     if end is not None:
         date_end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
     if end is None:
         date_end = datetime.strptime(
             datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
             "%Y-%m-%d %H:%M:%S"
         )
     calculation = date_end - date_start
     time = str(calculation).split(' ')[-1]
     hours, minutes, seconds = time.split(':')

     return f'''{str(calculation.days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s'''
