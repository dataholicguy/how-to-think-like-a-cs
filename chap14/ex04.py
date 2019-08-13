def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy     # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c):      # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False            # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def mirror_y(the_board):
    """ Mirror a solution in the Y axis """
    bd = the_board[:]
    bd.reverse()
    return bd

def mirror_x(the_board):
    """ Mirror a solution in the X axis """
    result = []
    for i in the_board:
        result.append(len(the_board)-1-i)
    return result

def rotate_ninety(the_board):
    """ Rotate a solution by 90-degrees anti-clockwise """
    enum_list = list(enumerate(the_board))
    sorted_enum = []
    for i in range(len(the_board)-1, -1, -1):
        for pair in enum_list:
            if pair[1] == i:
                sorted_enum.append(pair[0])
    return sorted_enum

def rotate_opposite(the_board):
    """ Rotate a solution by 180-degrees anti-clockwise """
    bd = the_board[:]
    bd.reverse()
    result = [len(the_board)-1-i for i in bd]
    return result

def rotate_more(the_board):
    """ Rotate a solution by 270-degrees anti-clockwise """
    return rotate_ninety(rotate_opposite(the_board))

def create_family(the_board):
    result = []
    result.append(the_board)
    result.append(mirror_y(the_board))
    result.append(mirror_x(the_board))
    result.append(rotate_opposite(the_board))
    result.append(rotate_ninety(the_board))
    e = rotate_ninety(the_board)[:]
    e.reverse()
    result.append(e)
    result.append(rotate_more(the_board))
    e = rotate_more(the_board)[:]
    e.reverse()
    result.append(e)
    return result

def same_family(list1, list2):
    family1 = create_family(list1)
    return list2 in family1
