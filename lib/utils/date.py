from collections import OrderedDict
from datetime import datetime, timedelta
from time import time
import re

def get_current_date_range():
    return {
        'from': datetime.now().strftime("%Y-%m-%d 00:00:00"),
        'to': datetime.now().strftime("%Y-%m-%d 23:59:59")
    }

def validate_date_pattern(date: str, pattern=r'\d\d\d\d-\d\d-\d\d'):
    m = re.search(pattern, date)
    if m:
        return True
    return False

def get_year_pattern():
    return "%Y-%m-%d"

def get_time_pattern():
    return "%H:%M:%S"

def get_datetime_pattern():
    return "%Y-%m-%d %H:%M:%S"

def get_formatted_difference(start, end: None):
     date_start = datetime.strptime(start, get_datetime_pattern())
     status = ""
     if end is not None:
         date_end = datetime.strptime(end, get_datetime_pattern())
     if end is None:
         date_end = datetime.strptime(
             datetime.now().strftime(get_datetime_pattern()), 
             get_datetime_pattern()
         )
         status = "[yellow](in progress)"
     calculation = date_end - date_start
     time = str(calculation).split(' ')[-1]
     hours, minutes, seconds = time.split(':')

     return f'''{str(calculation.days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s {status}'''

class DatePaginator:
    def __init__(self, date: str) -> None:
        self.__date = datetime.strptime(date, get_year_pattern())

    @property
    def next(self):
        self.__date += timedelta(days=1)
        return self.__date.strftime(get_year_pattern())

    @property
    def prev(self):
        self.__date -= timedelta(days=1)
        return self.__date.strftime(get_year_pattern())

    @property
    def curr(self):
        return datetime.now().strftime(get_year_pattern())

def get_difference(start, end):
    date_start = datetime.strptime(start, get_datetime_pattern())

    if end is None:
        date_end = datetime.strptime(
             datetime.now().strftime(get_datetime_pattern()), 
             get_datetime_pattern()
         )
    if end is not None:
        date_end = datetime.strptime(end, get_datetime_pattern())

    calculation = date_end - date_start
    time = str(calculation).split(' ')[-1]
    hours, minutes, seconds = time.split(':')

    return OrderedDict([
        ('days', int(calculation.days)),
        ('hours', int(hours)),
        ('minutes', int(minutes)),
        ('seconds', int(seconds))
    ])

    