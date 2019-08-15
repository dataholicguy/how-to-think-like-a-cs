import sys

print('Current recursion limit: {}'.format(sys.getrecursionlimit()))

sys.setrecursionlimit(10)
print('New recursion limit: {}'.format(sys.getrecursionlimit()))

def recursion_depth(number):
    print('{0}, '.format(number), end='')
    recursion_depth(number+1)

recursion_depth(0)
