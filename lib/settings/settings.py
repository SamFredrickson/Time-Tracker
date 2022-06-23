import json
import re

class JsonSettings:
    filename = 'settings.json'
    default_time = '00:00:00'
    def set_new_day(self, time: str):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                data['new_day_starts_at'] = time
                with open(self.filename, 'w') as file:
                    file.write(json.dumps(data))
        except FileNotFoundError:
            with open(self.filename, 'w') as file:
                file.write(json.dumps({'new_day_starts_at': time}))
    
    def get_new_day(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.filename, 'w') as file:
                data = {'new_day_starts_at': self.default_time}
                file.write(json.dumps(data))
                return data

    def get_avail_times_range(self):
        avail_times = []
        for n in range(24):
            if n >= 0 and n <= 9:
                avail_times.append(f'0{n}:00:00')
            else:
                avail_times.append(f'{n}:00:00')
        return avail_times