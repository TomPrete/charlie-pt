class Stack:

    def __init__(self):
        self.base = []

    def push(self, value):
        self.base.append(value)

    def pop(self):
        elem = self.base.pop()
        return elem

    def peek(self):
        return self.base[-1]

    def size(self):
        return len(self.base)

stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(7)
print(stack.base)
print(stack.pop())
print(stack.base)
print(stack.length_of_stack())
print(stack.peek())


