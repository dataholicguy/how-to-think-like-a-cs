def get_day_name(day_number):
    if day_number == 0:
        return 'Sunday'
    elif day_number == 1:
        return 'Monday'
    elif day_number == 2:
        return 'Tuesday'
    elif day_number == 3:
        return 'Wednesday'
    elif day_number == 4:
        return 'Thursday'
    elif day_number == 5:
        return 'Friday'
    elif day_number == 6:
        return 'Saturday'
    else:
        return 'Not Found'

day_numbers = [0, 1, 2, 3, 4, 5, 6]
start = 100
while start not in day_numbers:
    start = int(input('Starting day number: '))
    if start not in day_numbers:
        print('Start day number must in range [0, 6]')
length = int(input('Length of your stay: '))

print('Day of the week you will return on:', get_day_name((length + start) % 7))
