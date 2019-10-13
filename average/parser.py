import json
from datetime import datetime
from pytz import timezone

class TranslationDelivered:

    def __init__(self, json_input):
        json_obj = json.loads(json_input)

        self.timestamp = self.__process_datetime(json_obj['timestamp'])
        self.translation_id = json_obj['translation_id']
        self.source_language = json_obj['source_language']
        self.target_language = json_obj['target_language']
        self.client_name = json_obj['client_name']
        self.event_name = json_obj['event_name']
        self.duration = json_obj['duration']
        self.nr_words = json_obj['nr_words']
    
    def __process_datetime(self, date_time):
        date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
        tz = timezone('Europe/Lisbon')
        tz.localize(date_time_obj)
        return date_time_obj

def translation_delivered_parser(file_path):
    with open(file_path) as file:
        for line in file:
            x = TranslationDelivered(line)
            yield x
