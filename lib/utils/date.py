from collections import OrderedDict
from datetime import datetime, timedelta
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

def parse_time_from_date(date: str):
    m = re.search(r'\d\d:\d\d:\d\d', date)
    if m:
        return m.group()
    return False

def get_formatted_total(days: int, hours: int, minutes: int, seconds: int):
    delta = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    time = str(delta).split(' ')[-1]
    hours, minutes, seconds = time.split(':')
    
    return f'''{delta.days}d {hours}h {minutes}m {seconds}s'''

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

     days_formatted = f'{str(calculation.days)}d' if int(calculation.days) > 0 else ''
     hours_formatted = f'{int(hours)}h' if int(hours) > 0 else ''
     minutes_formatted = f'{int(minutes)}m' if int(minutes) > 0 else ''
     seconds_formatted = f'{int(seconds)}s' if int(seconds) > 0 else ''

     return f'''{days_formatted} {hours_formatted} {minutes_formatted} {seconds_formatted} {status}'''

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

    