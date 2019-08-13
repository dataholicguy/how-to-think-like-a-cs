import time

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    return dx == dy

def col_clashes(bs, c):
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False

def has_clashes(the_board):
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main(size):
    import random
    rng = random.Random()

    bd = list(range(size))
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1

t0 = time.clock()
main(8)
t1 = time.clock()
print('Time to find 10 solutions for 8x8 board: {} seconds.'.format(t1-t0))
print('-' * 100)
t2 = time.clock()
main(4)
t3 = time.clock()
print('Time to find 10 solutions for 4x4 board: {} seconds.'.format(t3-t2))
print('-' * 100)
t4 = time.clock()
main(12)
t5 = time.clock()
print('Time to find 10 solutions for 12x12 board: {} seconds.'.format(t5-t4))
print('-' * 100)
t6 = time.clock()
main(16)
t7 = time.clock()
print('Time to find 10 solutions for 16x16 board: {} seconds.'.format(t7-t6))
