class Stack:
    def __init__(self):
        self.stack = list()
    def is_empty(self):
        return len(self.stack) is None
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            raise IndexError("Stack is Empty")
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
print("top of stack before pop() operation : ",stack.top())
print("Size of stack before pop(_) operation : ",stack.size())
stack.pop()
print("top of stack  after pop() operation : ",stack.top())
print("Size of stack after pop(_) operation : ",stack.size())
# print(stack.top())
# print(stack.size())