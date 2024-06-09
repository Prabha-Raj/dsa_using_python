# stack by using list class witch is extending by stack class

class Stack(list):
    def is_empty(self):
        return len(self) is None
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'inset' in Stack")
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
s1.push(70)
print("Top of the Stack : ",s1.peek())
print("Size of the Stack : ",s1.size())
s1.pop()
print("Top of the Stack : ",s1.peek())
print("Size of the Stack : ",s1.size())