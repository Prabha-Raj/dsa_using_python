class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def insert_at_front(self,data):
        self.items.insert(0,data)
    def insert_at_rear(self,data):
        self.items.append(data)
    def delete_at_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is Empty")
    def delete_at_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque is Empty")
    
    def get_front(self):
        if not self.is_empty():
           return self.items[0]
        else:
            raise IndexError("Deque is Empty")
    def get_rear(self):
        if not self.is_empty():
           return self.items[-1]
        else:
            raise IndexError("Deque is Empty")
    def size(self):
        return len(self.items)
    
d1 = Deque()
d1.insert_at_front(10)
d1.insert_at_front(20)
d1.insert_at_front(30)
d1.insert_at_rear(40)
d1.insert_at_rear(50)
d1.insert_at_rear(60)
print("front = ",d1.get_front()," Rear = ",d1.get_rear())
print("size of Deque = ",d1.size())
d1.delete_at_front()
print("front = ",d1.get_front()," Rear = ",d1.get_rear())
print("size of Deque = ",d1.size())
d1.delete_at_rear()
print("front = ",d1.get_front()," Rear = ",d1.get_rear())
print("size of Deque = ",d1.size())