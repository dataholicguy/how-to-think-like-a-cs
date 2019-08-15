import time
import sys

sys.setrecursionlimit(100000)

alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

t0 = time.clock()
n = 10000
result = fib(n)
t1 = time.clock()

print('fib({0}): {1}, it took {2} seconds.'.format(n, result, t1-t0))
