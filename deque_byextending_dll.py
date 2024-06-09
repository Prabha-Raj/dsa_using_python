from dll import *
class Deque(Dll):
    def __init__(self):
        super().__init__()
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    def insert_front(self,data):
        if self.is_empty():
            self.insert_at_start(data)
            self.front = self.start
            self.rear = self.start
        else:
            self.insert_at_start(data)
            self.front = self.start
        self.item_count += 1
    def insert_rear(self,data):
        if self.is_empty():
            self.insert_at_end(data)
            self.front = self.start
            self.rear = self.start
        else:
            self.insert_at_end(data)
            self.rear = self.rear.next
        self.item_count += 1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front == self.rear:
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next
        self.item_count -= 1
        return super().delete_first()
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front == self.rear:
            self.rear = None
            self.front = None
        else:
            self.rear = self.rear.prev
        self.item_count -= 1
        return super().delete_first()
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
    

d1 = Deque()
d1.insert_front(5)
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