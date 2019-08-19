class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

# Traversing tree
def total(tree):
    """ Return sum of all tree node values"""
    if tree is None:
        return 0
    return total(tree.left) + total(tree.right) + tree.cargo

# Expression Tree
tree = Tree(Tree('+'), Tree(1), Tree('*', Tree(2), Tree(3))) # calculate (1 + 2 * 3)

# Preorder print
def preorder(tree):
    if tree is None:
        return
    print(tree.cargo, end=' ')
    preorder(tree.left)
    preorder(tree.right)

# Postorder print
def postorder(tree):
    if tree is None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.cargo, end=' ')

# Inorder print
def inorder(tree):
    if tree is None:
        return
    inorder(tree.left)
    print(tree.cargo, end=' ')
    inorder(tree.right)

# Indented print
def print_tree_indented(tree, level=0):
    if tree is None:
        return
    print_tree_indented(tree.right, level+1)
    print(' ' * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

# print('-' * 100)
# print('Preorder')
# preorder(tree)
# print()
#
# print('-' * 100)
# print('Inorder')
# inorder(tree)
# print()
#
# print('-' * 100)
# print('Postorder')
# postorder(tree)
# print()
#
# print('-' * 100)
# print('Print Indented')
# print_tree_indented(tree)
# print()

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        get_token(token_list, ')')
        return x
    else:
        x = token_list[0]
        if type(x) != type(0):
            return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree('*', a, b)
    return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree('+', a, b)
    return a
