from sll import *
class Stack:
    def __init__(self):
        self.stack = Sll()
        self.item_count = 0
    def is_empty(self):
        return self.stack.is_empty()
    def push(self,data):
        self.stack.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            data = self.stack.delete_first()
        if data is not None:
            self.item_count -= 1
        return data
    def peek(self):
        return self.stack.start
    def size(self):
        return self.item_count
    def insert_at_last(self):
        raise AttributeError("No Attribute 'insert_at_last' in stack")
    def insert_after(self,item,data):
        raise AttributeError("No Attribute 'insert_after' in stack")
    def delete_last(self):
        raise AttributeError("No Attribute 'delete_last' in stack")
    def delete_item(self,data):
        raise AttributeError("No Attribute 'delete_item' in stack")
    def search(self,data):
        raise AttributeError("No Attribute 'search' in stack")
    def insert_at_start(self,data):
        raise AttributeError("No Attribute 'insert_at_start' in stack")
    def insert_first(self):
        raise AttributeError("No Attribute 'delete_first' in stack")
    def print_list(self):
        raise AttributeError("No Attribute 'print_list' in stack")
    


s1 = Stack()
print()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print("size of stack : ",s1.size())
print("top of stack : ",s1.peek().item)
print("poped item of stack : ",s1.pop().item)
print()
print("size of stack : ",s1.size())
print("top of stack : ",s1.peek().item)