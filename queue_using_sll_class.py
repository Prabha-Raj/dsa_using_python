from sll import *
class Queue:
    def __init__(self):
        self.items = Sll()
        super().__init__()
        self.rear = None
        self.front = None
        self.item_count = 0
    def is_empty(self):
        return self.items.is_empty()
    def enqueue(self,data):
        if self.is_empty():
            self.items.insert_at_last(data)
            self.front = self.items.start
            self.rear = self.items.start    
        else:
            self.items.insert_at_last(data)
            self.rear = self.rear.next
        self.item_count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty so dequeue is no possible")
        elif self.rear == self.front:
            self.front = None
            self.rear = None
            self.items.delete_first()
        else:
            self.front = self.front.next
            self.items.delete_first()
        self.item_count -= 1
    def get_front(self):
        if not self.is_empty():
            return  self.front.item
        else:
            raise IndexError("Queue is empty so front is not present")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty so rear is not present")
    def size(self):
        return self.item_count
    
q1 = Queue()
try:
    # print(q1.get_front())
    # print(q1.get_front())
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.enqueue(40)
    q1.enqueue(50)
    q1.enqueue(60)
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
    print("size of Queue has now :  ",q1.size()," elements")
    q1.dequeue()
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
    print("size of Queue has now :  ",q1.size()," elements")
    q1.dequeue()
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
    print("size of Queue has now :  ",q1.size()," elements")
    q1.dequeue()
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
    print("size of Queue has now :  ",q1.size()," elements")
except IndexError as e:
    print(e)