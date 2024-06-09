class Queue:
    def __init__(self):
        self.queue = []
        # self.index = 0
        # self.front = self.queue[self.index]
        # self.rear = self.queue[self.index]
    def is_empty(self):
        return len(self.queue) is None
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self,):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            raise IndexError("Queue is underflow")
    def get_front(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            raise IndexError("Queue is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is Empty")
    def size(self):
        return len(self.queue)
    def insert(self,index,data):
        raise AttributeError("Queue han no Attribute 'insert' ")
    def pop(self):
        raise AttributeError("Queue han no Attribute 'pop' ")
    
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