def get_age():
    age = int(input('Please enter your age: '))
    if age < 0:
        # Create a new instance of an exeption
        my_error = ValueError('{0} is not a valid age'.format(age))
        raise my_error
    return age

age = get_age()
print(age)
