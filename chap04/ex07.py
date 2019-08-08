def sum_to(n):
    """Return the sum of all integer numbers up to and including n"""
    res = 0
    for i in range(1, n+1):
        res += i
    return res

print(sum_to(10))
