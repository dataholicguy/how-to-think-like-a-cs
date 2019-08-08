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

print(get_day_name(0))
