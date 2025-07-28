from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        assert self.tail is not None
        self.tail.next_node = new_node
        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    def at(self, index):
        if index < 0:
            print("Index out of bound")
            return None

        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index:
                return current_node
            current_node = current_node.next_node
            current_index += 1

        print("Index out of bound")
        return None

    def insert_at(self, value, index):
        list_size = self.size()

        if index < 0 or index > list_size:
            print("Index out of bound")
            return

        if index == 0:
            self.prepend(value)
            return

        if index == list_size:
            self.append(value)
            return

        previous_node = self.at(index - 1)
        if previous_node is None:
            print("Index out of bound")
            return

        new_node = Node(value)
        new_node.next_node = previous_node.next_node
        previous_node.next_node = new_node

    def remove_at(self, index):
        list_size = self.size()

        if index < 0 or index >= list_size:
            print("Index out of bound")
            return

        if index == 0:
            current_node = self.head
            if current_node is None:
                return
            self.head = current_node.next_node
            if self.head is None:
                self.tail = None
            current_node.next_node = None
            return

        previous_node = self.at(index - 1)
        if previous_node is None or previous_node.next_node is None:
            print("Index out of bound")
            return

        current_node = previous_node.next_node
        previous_node.next_node = current_node.next_node

        if current_node == self.tail:
            self.tail = previous_node

        current_node.next_node = None

    def pop(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current_node = self.head
        while current_node.next_node != self.tail:
            current_node = current_node.next_node

        current_node.next_node = None
        self.tail = current_node

    def contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def find(self, value):
        index = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return index
            current_node = current_node.next_node
            index += 1
        return None

    def to_string(self):
        node_value_strings = []
        current_node = self.head
        while current_node:
            node_value_strings.append(f"( {str(current_node.value)} )")
            current_node = current_node.next_node
        node_value_strings.append("null")
        return " -> ".join(node_value_strings)
