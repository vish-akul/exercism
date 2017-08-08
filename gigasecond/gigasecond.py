from datetime import datetime

from datetime import timedelta

def add_gigasecond(date1):
    date2 = date1 + timedelta(seconds =1000000000)
    return date2
