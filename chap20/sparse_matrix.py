matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print(matrix[(0, 3)] == 1)
print(matrix.get((1, 3), 0) == 0)   # use get method to get value of any element
print(matrix.get((2, 1), 0) == 2)   # the second argument is default if don't get anything
