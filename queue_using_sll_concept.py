class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self,front=None,rear=None):
        self.front = front
        self.rear = rear
        self.item_count = 0
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        n = Node(item=data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1
    def dequeue(self):
        if not self.is_empty():
            self.front = self.front.next
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            raise IndexError("No any data in the queue")
        self.item_count -= 1
    def get_front(self):
        if self.is_empty():
            raise IndexError("No any data in the queue")
        else:
            return self.front.item
            
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No any data in the queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
    
    
q1 = Queue()
# print(q1.get_front())
try:
    print(q1.get_front())
except IndexError as e:
    print(e)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print("Front of queue : ",q1.get_front())
print("Front of queue : ",q1.get_rear())
print("size of Queue has now :  ",q1.size()," elements")

try:
    q1.dequeue()
    print("size of Queue has now :  ",q1.size()," elements")
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
except IndexError as e:
    print(e)
            