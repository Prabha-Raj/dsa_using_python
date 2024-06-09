from sll import *
class Stack(Sll):
    def __init__(self):
        super().__init__(self)
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            data = self.start
            self.delete_first()
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.start
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return self.item_count

myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.push(50)
myStack.push(60)
myStack.push(70)
print("size of stack : ",myStack.size())
print("top of stack : ",myStack.peek().item)
print("poped item of stack : ",myStack.pop().item)
print("size of stack : ",myStack.size())
print("top of stack : ",myStack.peek().item)
    