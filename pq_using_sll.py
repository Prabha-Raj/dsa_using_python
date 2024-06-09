class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next
class PriorityQueue:
    def __init__(self,start=None):
        self.start = start
        self.item_count = 0
    def push(self,data,priority):
        new = Node(item=data,priority=priority)
        if not self.start or self.start.priority > priority:
            new.next = self.start
            self.start = new
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new.next = temp.next
            temp.next = new
        self.item_count += 1
    def pop(self):
        if self.start is None:
            raise IndexError("Priority Queue is Empty")
        item = self.start.item
        priority = self.start.priority
        self.start = self.start.next
        self.item_count -= 1
        return (item,priority)
    def is_empty(self):
        return self.start is None
    def size(self):
        return self.item_count

pq = PriorityQueue()
try:
    pq.push(data="Prabhakar",priority=1)
    pq.push(data="Prabha",priority=3)
    pq.push(data="Anjuly",priority=2)
    pq.push(data="Abhay",priority=5)
    pq.push(data="Shailandra",priority=6)
    pq.push(data="Shaurya",priority=8)
    pq.push(data="Arpita",priority=7)
    pq.push(data="Arush",priority=9)
    pq.push(data="Ansh",priority=12)
    pq.push(data="Ashu",priority=10)
    pq.push(data="Inder",priority=5)
    print("size of PriorityQueue : ",pq.size())
    print("order of Priority High to Low : ")
    while not pq.is_empty():
        tup = pq.pop()
        print("Priority = ",tup[1], "Data = ",tup[0])
except IndexError as e:
    print(e)