class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Cll:
    def __init__(self,last=None):
        self.last = last
    
    def is_empty(self):
        return self.last is None

    def insert_at_start(self,data):
        newNode = Node(item=data)
        if self.is_empty():
            newNode.next = newNode
            self.last = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode
    
    def insert_at_last(self,data):
        newNode = Node(item=data)
        if self.is_empty():
            newNode.next = newNode
            self.last = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode
            self.last = newNode
    def search(self,data):
        if self.is_empty():
            return None
        else:
            tempNode = self.last.next
            while tempNode is not self.last:
                if tempNode.item is data:
                    return tempNode
                tempNode = tempNode.next 
            if tempNode.item is data:
                return tempNode
            return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            newNode = Node(item=data,next=temp.next)
            temp.next = newNode
            if temp is self.last:
                self.last = newNode
    def print_list(self):
        if not self.is_empty():
            tempNode = self.last.next
            while tempNode is not self.last:
                # print("kk")
                print(tempNode.item,end=" ")
                tempNode = tempNode.next
            print(tempNode.item)
            # print("ll")
    
    def delete_first(self):
        if not self.is_empty():
            if self.last is self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next
    def delete_last(self):
        if not self.is_empty():
            if self.last is self.last.next:
                self.last = None
            else:
                tempNode = self.last.next
                while tempNode.next is not self.last:
                    tempNode = tempNode.next
                tempNode.next = self.last.next
                self.last = tempNode
                
    def delete_item(self,data):
        if not self.is_empty():
            if self.last is self.last.next:
                if self.last.item is data:
                    self.last = None
            elif self.last.next.item is data:
                self.delete_first()
            elif self.last.item is data:
                self.delete_last()
            else:
                tempNode = self.last.next
                while tempNode.next is not self.last:
                    if tempNode.next.item is data:
                        tempNode.next = tempNode.next.next
                        break
                    tempNode = tempNode.next
    def __iter__(self):
        if self.last is None:
            return CllItrator(None)
        else:
            return CllItrator(self.last.next)
class CllItrator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current is self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data
    
cll = Cll()
cll.insert_at_start(20)
cll.insert_at_start(10)
cll.insert_at_start(5)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_at_last(50)
cll.insert_after(cll.search(20),25)
cll.insert_after(cll.search(40),45)
cll.delete_first()
cll.delete_last()
cll.delete_item(20)
cll.print_list()
for i in cll:
    print(i,end=" ")
print()