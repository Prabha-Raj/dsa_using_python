class Queue(list):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            data = self.items[0]
            self.items.pop(0)
            return data
        else:
            raise IndexError("Queue is Empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is Empty")
    def size(self):
        return len(self.items)

q1 = Queue()
# print(q1.get_front())
try:
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
except IndexError as e:
    print(e)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)

try:
    print("Front of queue : ",q1.get_front())   
    print("Front of queue : ",q1.get_rear())
    print("size of Queue has now :  ",q1.size()," elements")
    q1.dequeue()
    print("size of Queue has now :  ",q1.size()," elements")
    print("Front of queue : ",q1.get_front())
    print("Front of queue : ",q1.get_rear())
except IndexError as e:
    print(e)
        