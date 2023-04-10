import datetime 
from exceptions import InvalidDateTimeFormat

class Utils:
    """
        UTILS
        This class contains all the utility functions for various data parsing/operations.
    """

    def parse_time(self, time: str, date: str) -> datetime:
        try:
            
            input_date = datetime.datetime.strptime(date, '%d/%m/%y')
            input_time = datetime.datetime.strptime(time, '%H:%M')
            return datetime.datetime.combine(input_date.date(), input_time.time())
            
        except ValueError:
            raise InvalidDateTimeFormat("Invalid input format. Please enter time and date in the format HH:MM and DD/MM/YY")