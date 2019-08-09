def triangular_number(n):
    """ Return the n th triangular number. """
    if n == 1:
        return 1
    elif n > 1:
        return triangular_number(n-1) + n

def print_triangular_numbers(n):
    """ Print out the first n triangular numbers. """
    for i in range(1, n+1):
        print(i, "\t", triangular_number(i))

print_triangular_numbers(5)
