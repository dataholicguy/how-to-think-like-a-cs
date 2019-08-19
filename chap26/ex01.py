# Implement Queue ADT using Python list
import time

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        cargo = self.items[0]
        del self.items[0]
        return cargo

class Node:
    def __init__(self, cargo=0, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

t0 = time.clock()
q = Queue()
for item in [1, 2, 3, 4, 5]:
    q.insert(item)
t1 = time.clock()
print('Time for Queue using Python list: {0} seconds.'.format(t1-t0))

t2 = time.clock()
iq = ImprovedQueue()
for item in [1, 2, 3, 4, 5]:
    iq.insert(item)
t3 = time.clock()
print('Time for Improved Queue: {0} seconds.'.format(t3-t2))

print('-' * 100)
while not q.is_empty():
    print(q.remove())

print('-' * 100)
while not iq.is_empty():
    print(iq.remove())
