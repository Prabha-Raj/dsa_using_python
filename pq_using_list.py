class PriorityQueue:
    def __init__(self):
        self.itmes = []
    def is_empty(self):
        return len(self.itmes) == 0
    def push(self,data,priority):
        index = 0
        # while not self.is_empty() and priority<self.itmes[index][1]:  #-- it will insert higher priority first
        while index<len(self.itmes) and priority>=self.itmes[index][1]:  #-- it will insert higher priority last
            index += 1
        self.itmes.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        # return self.itmes.pop() # -- if you insert higher priority first then you will use this
        return self.itmes.pop(0) # -- if you insert higher priority last then you will use this
    def size(self):
        return len(self.itmes)

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
    print("size of PriorityQueue : ",pq.size())
    print("order of Priority High to Low : ")
    while not pq.is_empty():
        tup = pq.pop()
        print("Priority = ",tup[1], "data = ",tup[0])
except IndexError as e:
    print(e)