def readposint():
    pos_int = int(input('Please enter a positive number: '))
    if pos_int <= 0:
        error1 = ValueError('{0} is not a positive number.'.format(pos_int))
        raise error1
    elif type(pos_int) != type(1):
        error2 = ValueError('{0} is not an integer.'.format(pos_int))
        raise error2
    return pos_int

num = readposint()
print(num)      # If no error, display input number
