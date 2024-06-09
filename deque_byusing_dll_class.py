from dll import *
class Deque:
    def __init__(self):
        super().__init__()
        self.items = Dll()
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.items.is_empty()
    def insert_front(self,data):
        if self.is_empty():
            self.items.insert_at_start(data)
            self.rear = self.items.start 
        else:
            self.items.insert_at_start(data)
        self.front = self.items.start
        self.item_count += 1
    def insert_rear(self,data):
        if self.is_empty():
            self.items.insert_at_end(data)
            self.front = self.items.start
        else:
            self.items.insert_at_end(data)
        self.rear = self.rear.next
        self.item_count += 1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.items.delete_first()
        self.item_count -= 1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")        
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
        self.items.delete_last()
        self.item_count -= 1
    def get_front(self):
        if self.front is not None:
            return self.front.item
        else:
            raise IndexError("Deque is Empty")
    def get_rear(self):
        if self.rear is not None:
            return self.rear.item
        else:
            raise IndexError("Deque is Empty")
    def size(self):
        return self.item_count

d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_front(35)
d1.insert_rear(40)
d1.insert_rear(50)
d1.insert_rear(60)
d1.insert_rear(70)
try :
    d1.insert_rear(80)
    print("front = ",d1.get_front()," Rear = ",d1.get_rear())
    print("size of Deque = ",d1.size())
    d1.delete_front()
    print("front = ",d1.get_front()," Rear = ",d1.get_rear())   
    print("size of Deque = ",d1.size())
    d1.delete_rear()
    print("front = ",d1.get_front()," Rear = ",d1.get_rear())
    print("size of Deque = ",d1.size())
except IndexError as e:
    print(e)