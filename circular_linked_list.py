class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class CircularLinkedList:
    def __init__(self,last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def print_list(self):
        if self.last is not None:
            tempNode = self.last.next
            while tempNode is not self.last:
                print(tempNode.item,end=" ")
                tempNode = tempNode.next
            print(tempNode.item)

    def insert_at_first(self,data):
        newNode = Node(item=data)
        if not self.is_empty():
            newNode.next = self.last.next
            self.last.next = newNode
        else:
            newNode.next = newNode
            self.last = newNode

    def insert_at_last(self,data):
        newNode = Node(item=data)
        if self.is_empty():
            # print('ii')
            newNode.next = newNode
            self.last = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode
            self.last = newNode
    def search(self,searchItem):
        if not self.is_empty():
            tempNode = self.last
            while tempNode is not None:
                if tempNode.item is searchItem:
                    return tempNode
                if tempNode.next is self.last:
                    # print("iiii")
                    break
                tempNode = tempNode.next
                
    def insert_after(self,nodeObject,data):
        if not self.is_empty():
            tempNode = self.last
            while tempNode.next is not None:
                if tempNode == nodeObject:
                    newNode = Node(item=data,next=tempNode.next)
                    tempNode.next = newNode
                    break
                tempNode = tempNode.next
    def delete_at_first(self):
        if not self.is_empty():
            if self.last is self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_at_last(self):
        if not self.is_empty():
            if self.last is self.last.next:
                self.last = None
            else:
                tempNode = self.last
                while tempNode is not None:
                    if tempNode.next is self.last:
                        tempNode.next = self.last.next
                        self.last = tempNode
                        break
                    if tempNode.next is self.last:
                        break
                    tempNode = tempNode.next
    def delete_item(self,nodeObject):
        if not self.is_empty():
            if self.last is self.last.next:
                if self.last is nodeObject:
                    self.last = None
            else:
                tempNode = self.last
                while tempNode is not nodeObject:
                    if tempNode.next is nodeObject:
                        tempNode.next = tempNode.next.next
                        break
                    if tempNode.next is self.last:
                        break
                    tempNode = tempNode.next
                tempNode = self.last
                while tempNode is not None:
                    if tempNode.next is self.last and self.last is nodeObject:
                        # print("yes",tempNode.next.item)
                        tempNode.next = self.last.next
                        self.last = tempNode
                        break
                    if tempNode.next is self.last:
                        break
                    tempNode = tempNode.next
    def __iter__(self):
        return CllItrator(self.last.next)
class CllItrator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.status = False
    def __iter__(self):
        return self
    def __next__(self):      
        if not self.current:
            raise StopIteration
        elif self.current is self.start and self.status is True:
            raise StopIteration
        else:
            self.status = True
            data = self.current.item
            self.current = self.current.next
            return data


                


myCList = CircularLinkedList()
print("list is empty : -- : ",myCList.is_empty())

myCList.insert_at_first(40)
myCList.insert_at_first(30)
myCList.insert_at_first(20)
myCList.insert_at_first(10)
print("print list after inserting items at first : ")
myCList.print_list()


myCList.insert_at_last(50)
myCList.insert_at_last(60)
myCList.insert_at_last(70)
myCList.insert_at_last(80)
print("print list after inserting items at last : ")
myCList.print_list()

# insertin in mid
searchObject = myCList.search(50)
myCList.insert_after(searchObject,55)
print("print list after inserting item after some items : ")
myCList.print_list()

# deleting first Node
myCList.delete_at_first()
print("print list after deletion first item: ")
myCList.print_list()

# deletting last Node
myCList.delete_at_last()
print("print list after deletion last item: ")
myCList.print_list()

# deleting specific Node
nodeObject = myCList.search(50)
myCList.delete_item(nodeObject)
print("print list after deletion last item: ")
myCList.print_list()

print("print list by uging Itrator class : ")
for item in myCList:
    print(item,end=" ")

