class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, node=None):
        if node:
            node.next = self.head
            self.head = node

    def search_node(self, data=None):
        if data:
            curr_node = self.head
            if curr_node:
                if curr_node.data == data:
                    return data
                curr_node = curr_node.next

            return None

