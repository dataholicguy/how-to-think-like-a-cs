import time

def fib(n):
    if n <= 1:
        return n
    else:
        result = 1
        prev = 1
        for i in range(2, n):
            tmp = result
            result += prev
            prev = tmp
    return result

t0 = time.clock()
n = 200
result = fib(n)
t1 = time.clock()

print('fib({0}) = {1}, ({2:.2f} secs)'.format(n, result, t1-t0))
