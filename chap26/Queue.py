class Node:
    def __init__(self, cargo=0, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):        # linear time (not good)
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):               # constant time
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo
