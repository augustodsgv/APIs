months_str_to_int = {
    1 : 'jan',
    2 : 'feb',
    3 : 'mar',
    4 : 'apr',
    5 : 'may',
    6 : 'jun',
    7 : 'jul',
    8 : 'aug',
    9 : 'sep',
    10 :'oct',
    11 :'nov',
    12 :'dec'
}

month_days_count = {
    1 : 31,
    2 : None,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 :31,
    11 :30,
    12 :31
}

class Date:
    def __init__(self, day : int, month : int, year : int):
        if Date.is_valid_year(year):
            self.year = year
        else:
            raise Exception(f'Invalid year {year}')

        if Date.is_valid_month:
            self.month = month
        else:
            raise Exception(f'Invalid month {month}')
        
        if Date.is_valid_day(day, month, year):
            self.day = day
        else:
            raise Exception(f'Invalid day {day}')
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date): return False
        if self.day != other.day: return False
        if self.month != other.month: return False
        if self.year != other.year: return False
        return True
    
    # Month property that transcribes 
    @property
    def month_str(self) -> str:
        return months_str_to_int[self.month]

    ## Date validators ##
    @classmethod
    def is_valid_day(cls, day: int, month: int, year: int):
        # Testing if it's a positive number
        if day <= 0:
            return False

        # Testing if it's not on february, that needs leap year treatment
        if month != 2:
            return day <= month_days_count[month]

        # Testing if it's a leap year
        # every 4 year there is a leap year, except if it's a year that ends with 100.
        # Even though, if it's a year that is divisible by 400, it's a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # is leap
            return day <= 29
        else:  # is not leap
            return day <= 28

    @classmethod
    def is_valid_month(cls, month: int):
        return month > 0 and month <= 12

    @classmethod
    def is_valid_year(cls, year: int):
        return True

    # Returns a date str formated
    def get_date(self, format : str = 's') -> str:
        if format == 's':       # Short format
            return '{}/{}/{}'.format(self.month, self.day, self.year)
        elif format == 'l':     # Long format
            return '{} {}, {}'.format(self.day, self.month_str, self.year)
        else:
            raise Exception(f'Invalid date format{format}')
        
    # TODO
    def diff(self, other : object):
        pass
        # Years diff