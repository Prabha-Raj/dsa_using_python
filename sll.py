class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        newNode=Node(data,self.start)
        self.start=newNode

    def insert_at_last(self,data):
        newNode=Node(data)
        if not self.is_empty():
            tempNode = self.start
            while tempNode.next is not None:
                tempNode=tempNode.next
            tempNode.next=newNode
        else:
            self.start=newNode
    def search(self,item):
        tempNode = self.start
        while tempNode is not None:
            if tempNode.item == item:
                return tempNode
            tempNode = tempNode.next
        return None
    def insert_after(self,tempNode,data):
        if tempNode is not None:
            newNode=Node(data,tempNode.next)
            tempNode.next=newNode
    def print_list(self):
        tempNode=self.start
        print('[ ',end='')
        while tempNode is not None:
            print(tempNode.item,end='')
            tempNode=tempNode.next
            if tempNode is not None:
                print(end=', ')
            else:
                print(end='')
        print(' ]')
        # print(tempNode.item)
    def delete_first(self):
        if self.start is not None:
            # tempNode=self.start
            # self.start=tempNode.next
            data = self.start
            self.start=self.start.next
            return data
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None

        else:
            tempNode = self.start
            while tempNode.next.next is not None:
                tempNode = tempNode.next
            tempNode.next=None
    def delete_item(self,item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == item:
                self.start = None
        else:
            tempNode=self.start
            if tempNode.item == item:
                self.start=tempNode.next
            else:
                while tempNode.next is not None:
                    if tempNode.next.item == item:
                        tempNode.next=tempNode.next.next
                        break
                    tempNode = tempNode.next
    def __iter__(self):
        return SllItrator(self.start)
        
class SllItrator:
    def __init__(self,start):
        self.current = start
    def __iter__(self,):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data

myList = Sll()
myList.insert_at_start(50)
myList.insert_at_start(40)
n=myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
item = myList.search(20)
myList.insert_after(item,25)
item = myList.search(30)
myList.insert_after(item,35)
myList.insert_at_last(60)
myList.insert_at_last(70)
myList.delete_first()
myList.delete_last()
myList.delete_item(item)
myList.delete_item(10)
myList.delete_item(60)
myList.delete_item(25)

# myList.print_list()
# # print("")
# for i in myList:
#     print(i,end=" ")

