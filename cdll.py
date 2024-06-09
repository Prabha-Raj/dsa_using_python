class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Cdll:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start is None
    def instert_at_start(self,data):
        newNode = Node(item=data)
        if self.is_empty() and data is not None:
            newNode.next = newNode
            newNode.prev = newNode
            # self.start = newNode
        else:
            newNode.next = self.start
            newNode.prev = self.start.prev
            self.start.prev.next = newNode
        self.start = newNode
    def instert_at_last(self,data):
        newNode = Node(item=data)
        if self.is_empty() and data is not None:
            newNode.next = newNode
            newNode.prev = newNode
            self.start = newNode
        else:
            newNode.next = self.start
            newNode.prev = self.start.prev
            self.start.prev.next = newNode
            self.start.prev = newNode
        # self.start = newNode
    def search(self,data):
        if not self.is_empty() and data is not None:
            tempNode = self.start
            if tempNode.item is data :
                return tempNode
            else:
                tempNode = tempNode.next
                while tempNode is not self.start:
                    if tempNode.item is data:
                        return tempNode
                    tempNode = tempNode.next 
            return None
    def insert_after(self,item,data):
        tempNode = self.search(item)
        if not self.is_empty() and tempNode is not None and data is not None:        
            newNode = Node(item=data)
            newNode.next = tempNode.next
            newNode.prev = tempNode
            tempNode.next.prev = newNode
            tempNode.next = newNode
    def print_list(self):
        if self.start is not None:
            tempNode = self.start
            while tempNode.next is not self.start:
                print(tempNode.item,end=" ")
                tempNode = tempNode.next
            print(tempNode.item)
    def delete_first(self):
        if self.start is not None:
            if self.start is self.start.next:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
    def delete_last(self):
        if self.start is not None:
            if self.start is self.start.next:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    def delete_item(self,data):
        tempNode = self.search(data)
        if self.start is not None and tempNode is not None:
            if self.start is tempNode:
                self.delete_first()
            elif self.start.prev is tempNode:
                self.delete_last() 
            else:
                tempNode.prev.next = tempNode.next
                tempNode.next.prev = tempNode.prev
    def __iter__(self):
        return  CdllItrator(self.start)

class CdllItrator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.flag = False
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        elif self.current is self.start and self.flag is True:
            raise StopIteration
        else:
            self.flag = True
            data = self.current.item
            self.current = self.current.next
            return data

myCDLList = Cdll()
myCDLList.instert_at_start(40)
myCDLList.instert_at_start(30)
myCDLList.instert_at_start(20)
myCDLList.instert_at_start(10)
myCDLList.instert_at_last(50)
myCDLList.instert_at_last(60)
myCDLList.instert_at_last(70)
myCDLList.instert_at_last(80)
myCDLList.insert_after(40,45)
myCDLList.delete_first()
myCDLList.delete_last()
myCDLList.delete_item(45)
myCDLList.print_list()
print("Using Itrator ")
for item in myCDLList:
    print(item,end=" ")