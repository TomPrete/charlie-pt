class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def add(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        return new_node

    def remove(self, value):
        current_node = self.head
        previous_node = None
        if current_node.value == value:
            self.head = current_node.next_node
        else:
            while current_node.value != value:
                previous_node = current_node
                current_node = current_node.next_node
            previous_node.next_node = current_node.next_node
            self.length -= 1
        return self.head

    def length_ll(self):
        return self.length



ll = LinkedList()
ll.add(4)
print(ll.head.value)
ll.add(7)
ll.add(2)
ll.add(8)
ll.add(6)
ll.add(9)
ll.add(1)
print(ll.head.next_node.value)
print(ll.head.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.next_node.next_node.next_node.value)
print('LENGTH: ', ll.length_ll())
print("--- REMOVE ---")
ll.remove(8)
print(ll.head.value)
print(ll.head.next_node.value)
print(ll.head.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.next_node.value)
print(ll.head.next_node.next_node.next_node.next_node.next_node.value)
print('LENGTH: ', ll.length_ll())
