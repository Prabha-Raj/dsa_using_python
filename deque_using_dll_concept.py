class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count == 0
    def insert_at_front(self,data):
        n = Node(prev=None,item=data,next=self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1
    def insert_at_rear(self,data):
        n = Node(item=data,prev=self.rear,next=None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1
    def delete_at_front(self):
        if not self.is_empty():
            data = self.front.item
            self.front = self.front.next
            self.front.prev = None
            self.item_count -= 1
            return data
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            raise IndexError("Deque is empty")
      
    def delete_at_rear(self):
        if not self.is_empty():
            data = self.rear.item
            self.rear = self.rear.prev
            self.rear.next = None
            self.item_count -= 1
            return data
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            raise IndexError("Deque is empty")

    def size(self):
        return self.item_count

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Deque is empty")
    
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
