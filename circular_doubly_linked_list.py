class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class CircularDoublyLinkedList:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start is None
    def print_list(self):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not self.start.prev:
                print(tempNode.item,end=" ")
                tempNode = tempNode.next
            print(tempNode.item)
    def search(self,data):
        if not self.is_empty():
            tempNode = self.start
            flag = False
            while tempNode is not self.start.prev:
                if tempNode.item is data:
                    flag = True
                    return tempNode
                tempNode = tempNode.next
            if tempNode.item is data:
                flag = True
                return tempNode
            if not flag:
                return None
    def insert_at_start(self,data):
        newNode = Node(item=data)
        if self.is_empty():
            newNode.next = newNode
            newNode.prev = newNode
            self.start = newNode
        else:
            newNode.next = self.start
            newNode.prev = self.start.prev
            self.start.prev.next = newNode
            self.start.prev = newNode
            self.start = newNode
    def insert_at_last(self,data):
        newNode = Node(item=data)
        if self.is_empty():
            self.insert_at_start(data)
        else:
            newNode.next = self.start
            newNode.prev = self.start.prev
            self.start.prev.next = newNode
            self.start.prev = newNode
    def insert_after(self,after,data):
        newNode = Node(item=data)
        after = self.search(after)
        # print(after.item)
        if not self.is_empty() and after is not None:
            if after == self.start.prev:
                self.insert_at_last(data)
            else:
                newNode.next = after.next
                newNode.prev = after
                after.next.prev = newNode
                after.next = newNode
    def delete_first(self):
        if not self.is_empty():
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next
    def delete_last(self):
        if not self.is_empty():
            if self.start is self.start.next:
                self.delete_first()
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    def delete_item(self,data):
        if not self.is_empty():
            tempNode = self.search(data)
            if tempNode is self.start:
                self.delete_first()
            elif tempNode is self.start.prev:
                self.delete_last()
            else:
                tempNode.prev.next = tempNode.next
                tempNode.next.prev = tempNode.prev
    def __iter__(self):
        return CircularDoublyLinkedListItrator(self.start)
class CircularDoublyLinkedListItrator:
    def __init__(self,start):
        self.start = start
        self.current = start
        self.flag = False
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        elif self.current is self.start and self.flag is True:
            raise StopIteration
        else:
            self.flag = True
            data = self.current.item
            self.current = self.current.next
            return data


mylist = CircularDoublyLinkedList()
print("items inserted by using insert at start function : ")
mylist.insert_at_start(40)
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.print_list()
print("items inserted by using insert at last function : ")
mylist.insert_at_last(50)
mylist.insert_at_last(60)
mylist.insert_at_last(70)
mylist.insert_at_last(80)
mylist.print_list()
print("items inserted by using insert after function : ")
mylist.insert_after(50,55)
mylist.print_list()
print("item delete by using delete first function : ")
mylist.delete_first()
mylist.print_list()
print("item delete by using delete last function : ")
mylist.delete_last()
mylist.print_list()
print("item delete by using delete Item function : ")
mylist.delete_item(50)
mylist.print_list()
print("Printing myList by using Itrator Class : ")
for item in mylist:
    print(item,end=" ")