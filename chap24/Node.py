class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def print_list(node):
    while node is not None:
        print(node, end=' ')
        node = node.next
    print()

def print_backward(list):
    if list is None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=' ')

def remove_second(list):
    if list is None:
        return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.list = None
    return second

def print_backward_nicely(list):
    print('[', end=' ')
    print_backward(list)
    print(']')

def print_list_nicely(list):
    result = []
    while list is not None:
        result.append(list.cargo)
        list = list.next
    print('{0}'.format(result))

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print_list_nicely(node1)
