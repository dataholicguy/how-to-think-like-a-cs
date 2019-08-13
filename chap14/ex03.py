# Adapt the queens program so that we keep
# a list of solutions that have already printed,
# so that we don’t print the same solution more than once.

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    return dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False

def has_clashes(the_board):
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main():
    import random
    rng = random.Random()
    rng.seed(50)            # Add this line to solve

    bd = list(range(8))
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print('Found solution {0} in {1} tries.'.format(bd, tries))
            tries = 0
            num_found += 1

main()
