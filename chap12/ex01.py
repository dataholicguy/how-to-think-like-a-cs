import calendar
cal = calendar.TextCalendar()   # Create an instance
cal.setfirstweekday(calendar.THURSDAY)
cal.pryear(2012)
print('-' * 75)

def print_birth_month():
    birth_month = int(input('The month in which your birthday occurs: '))
    cal.prmonth(2012, birth_month)

print_birth_month()
print('-' * 75)

print('Is 2012 leap year?', calendar.isleap(2012))
