class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=' ')


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print('[', end=' ')
        if self.head is not None:
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1
