from datetime import datetime
from datetime import timedelta

class AverageCalc:

    def __init__(self, window_size):
        self.__timestamp_duration_list =[]
        self.__delta_increment = timedelta(minutes=1)
        self.__delta_window = timedelta(minutes=int(window_size))
        self.__overlap_list = []
    
    def add_tranlation_delivered(self, tranlation_delivered):
        """Record the translation delivered events"""   
        button = self.__get_time_until_minutes(tranlation_delivered.timestamp) + self.__delta_increment
        top = button + self.__delta_window
        self.__timestamp_duration_list.append((button, top, tranlation_delivered.duration))
            
    def cal_avg_delivered_time(self):
        if len(self.__timestamp_duration_list) > 0:

            time_reference = self.__get_time_until_minutes(self.__timestamp_duration_list[0][0]) - self.__delta_increment
            
            while len(self.__timestamp_duration_list) > 0:
                self.__update_overlap_list(time_reference)
                self.__update_timestamp_duration_list()

                yield (str(time_reference), self.__calc_overlap_average())                
                
                time_reference += self.__delta_increment

    def __update_overlap_list(self, reference):
        """Keep the list with events in the average time window"""
        self.__remove_element_out_of_range(reference)

        for item in self.__timestamp_duration_list:
            if item[0] > reference:
                break
            self.__overlap_list.append(item)
    
    def __remove_element_out_of_range(self, reference):
        result = []
        for item in self.__overlap_list:
            if item[1] > reference:
                result.append(item)
        self.__overlap_list = result

    def __update_timestamp_duration_list(self):
        """Remove from timestamp_duration the overlap_list's item"""
        for item in self.__overlap_list:
            if item in self.__timestamp_duration_list:
                self.__timestamp_duration_list.remove(item)

    def __calc_overlap_average(self):
        average = 0
        if len(self.__overlap_list) > 0:
            size = len(self.__overlap_list)
            amount = 0
            for item in self.__overlap_list:
                if item[0] < item[1]:
                    amount += item[2]
            average = amount/size
            if int(average) == average:
                average = int(average)
                
        return average
   
    def __get_time_until_minutes(self, timestamp):
        return  datetime(year=timestamp.year,
                    month=timestamp.month,
                    day=timestamp.day,
                    hour=timestamp.hour,
                    minute=timestamp.minute)
