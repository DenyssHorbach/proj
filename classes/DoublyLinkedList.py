from classes.Node import *


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            raise IndexError("Index out of range")

        current = self.head
        counter = 0

        while current is not None:
            if counter == index:
                return current.data
            current = current.next
            counter += 1
        raise IndexError("Index out of range")

    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            raise IndexError("Negative index")
        new_node = Node(data)
        if index == 0:                  #add to head (0 pos)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return
        current = self.head
        counter = 0
        while current is not None and counter < index:
            current = current.next
            counter += 1

        if current is None and counter == index:       #to end (last pos)
            self.append(data)
            return

        if current is not None:
            new_node = Node(data)
            new_node.next = current
            new_node.prev = current.prev
            if current.prev is not None:
                current.prev.next = new_node
            current.prev = new_node
            return
        raise IndexError("Index out of range")


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print('end!')
