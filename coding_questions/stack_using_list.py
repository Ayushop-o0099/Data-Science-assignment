class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
s = Stack()
s.push(10)
s.push(20)
print("Top element:", s.peek())
s.pop()
print("Top element after pop:", s.peek())
