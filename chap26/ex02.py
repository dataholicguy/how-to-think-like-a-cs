# Implement Priority Queue ADT using a linked list

import time

class Node:
    def __init__(self, cargo=0, next=None, prev=None):
        self.cargo = cargo
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.cargo)

class PriorityQueue:
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
            node.prev = last
            self.last = node
        self.length += 1

    def remove(self):
        maxi = self.head.cargo
        node = self.head
        while node:
            if node.cargo > maxi:
                maxi = node.cargo
                ptr = node
            node = node.next
        if maxi == self.head.cargo:
            self.head = self.head.next
        else:
            prev = ptr.prev
            prev.next = ptr.next
        self.length -= 1
        return maxi


# Priority Queue implement using Python list
class PriorityQueueList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

pq = PriorityQueue()
t0 = time.clock()
for item in [1, 2, 3, 4, 5]:
    pq.insert(item)
t1 = time.clock()
print('Time for priority queue using linked list: {0} seconds.'.format(t1-t0))

pql = PriorityQueueList()
t2 = time.clock()
for item in [1, 2, 3, 4, 5]:
    pql.insert(item)
t3 = time.clock()
print('Time for priority queue using Python list: {0} seconds.'.format(t3-t2))

print('-' * 100)
while not pq.is_empty():
    print(pq.remove())

print('-' * 100)
while not pql.is_empty():
    print(pql.remove())
