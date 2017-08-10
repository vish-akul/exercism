import calendar
from datetime import date

days = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday', 3 : 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}

def meetup_day(year, month, day, filt):

    count = 0

    if filt == 'teenth':
        for i in range(13,20):
            if days[calendar.weekday(year, month, i)] == day:
                d = i
    if filt == '1st':
        for i in range(1,calendar.monthrange(year,month)[1]):
            if days[calendar.weekday(year, month, i)] == day:
                d = i
                break
    if filt == '2nd':
        for i in range(1,calendar.monthrange(year,month)[1]):
            if days[calendar.weekday(year, month, i)] == day:
                count += 1
            if count == 2:
                d = i
                break
    if filt == '3rd':
        for i in range(1,calendar.monthrange(year,month)[1]):
            if days[calendar.weekday(year, month, i)] == day:
                count += 1
            if count == 3:
                d = i
                break
    if filt == '4th':
        for i in range(1,calendar.monthrange(year,month)[1]):
            if days[calendar.weekday(year, month, i)] == day:
                count += 1
            if count == 4:
                d = i
                break
    if filt == '5th':
        for i in range(1,calendar.monthrange(year,month)[1]):
            if days[calendar.weekday(year, month, i)] == day:
                count += 1
            if count == 5:
                d = i
                break
    if filt == 'last':
        for i in range(calendar.monthrange(year,month)[1],1,-1):
            if days[calendar.weekday(year, month, i)] == day:
                d = i
                break
    if d > calendar.monthrange(year,month)[1]:
        raise MeetupDayException()

    return date(year, month, d)
