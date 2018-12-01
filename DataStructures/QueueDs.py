class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head:
            r = self.head.val
            self.head = self.head.next
            return r

    def get_as_list(self):
        t = self.head
        queue_list = []
        while t:
            queue_list.append(t.val)
            t = t.next
        return queue_list

    def print_list(self):
        print(self.get_as_list())
