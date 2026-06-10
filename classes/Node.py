from classes.Vehicle import Vehicle

class Node:
    def __init__(self, data: Vehicle):
        self.data = data
        self.next = None
        self.prev = None
