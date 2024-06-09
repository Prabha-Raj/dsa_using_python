class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self,start=None):
        self.start = start
        self.item_count = 0
    def is_empty(self):
        return self.item_count == 0
    def push(self,data):
        newNode = Node(item=data,next=self.start)
        self.start = newNode
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return self.item_count

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
print("top of stack before pop() operation : ",stack.peek())
print("Size of stack before pop(_) operation : ",stack.size())
print("poped item is : ",stack.pop())
print("top of stack  after pop() operation : ",stack.peek())
print("Size of stack after pop(_) operation : ",stack.size())
