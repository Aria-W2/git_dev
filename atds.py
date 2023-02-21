#1/usr/bin/env python 3
"""

Describes the Data Structures used in the Advanced Topics
"""

__author__ = "Aria Wang"
__version__ = "the date" 


class Stack(object):
    """Describes a stack with traditional peel, pop, push methods, as a well as size() and isEmpty()"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds an item on the list, ie. the top of the stack"""
        self.stack.append(item)

    def pop(self):
        """Returns the last item on the list, ie. the top of the stack"""
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

class Queue(object):
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return len(self.queue) == 0

class Deque(object):
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)

    def remove_rear(self):
        if len(self.deque) > 0:
            return self.deque.pop()

    def size(self):
        return len(self.deque)

    def is_empty(self): 
        return len(self.deque) == 0

