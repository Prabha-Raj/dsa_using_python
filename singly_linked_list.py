class Node:
    def __init__(self,item=None,next=None):
        self.next=next
        self.item=item
class SingleLinkedList:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        if self.start is not None:
            return False
        else:
            return True
    def print_list(self):
        tempNode = self.start
        while tempNode is not None:
            print(tempNode.item,end=" ")
            tempNode=tempNode.next
    def insert_at_first(self,data):
        newNode = Node(data)
        if self.start is None:
            self.start=newNode
        else:
            newNode.next=self.start
            self.start=newNode
    def insert_at_last(self,data):
        newNode = Node(data)
        if self.start is None:
            self.start=newNode
        elif self.start.next is None:
            self.start.next = newNode
        else:
            tempNode = self.start
            while tempNode.next is not None:
                tempNode = tempNode.next
            tempNode.next = newNode
    def insert_after(self,item,data):
        newNode = Node(data)
        if not self.is_empty():
            tempNode = self.start
            while tempNode.next is not None:
                if tempNode.item is item:
                    newNode.next= tempNode.next
                    tempNode.next = newNode
                    break
                tempNode = tempNode.next
    def search(self,data):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                if tempNode.item == data:
                    return tempNode
                tempNode = tempNode.next
    def delete_first(self):
        if not self.is_empty():
            self.start=self.start.next
    def delete_last(self):
        if not self.is_empty():
            if self.start.next is None:
                self.start = None
            else:
                tempNode = self.start.next
                while tempNode is not None:
                    if tempNode.next.next is None:
                        tempNode.next = None
                    tempNode = tempNode.next
    def delete_item(self,data):
        if not self.is_empty():
            if self.start.item is data:
                self.start=self.start.next
            elif self.start.next.item is data:
                self.start.next = self.start.next.next
            else:
                tempNode = self.start
                while tempNode.next is not None:
                    if tempNode.next.item == data:
                        tempNode.next = tempNode.next.next
                        break
                    tempNode= tempNode.next
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


                    


        




myLinkedList = SingleLinkedList()
print("Item inserte by using insert_at_first function : ")
myLinkedList.insert_at_first(10)
myLinkedList.insert_at_first(20)
myLinkedList.insert_at_first(30)
myLinkedList.insert_at_first(40)
myLinkedList.print_list()
print("")
print("Item inserte by using insert_at_last function : ")
myLinkedList.insert_at_last(50)
myLinkedList.insert_at_last(60)
myLinkedList.insert_at_last(70)
myLinkedList.insert_at_last(80)
myLinkedList.insert_at_last(90)
myLinkedList.print_list()
print("")
print("Item inserte by using insert_after function : ")
myLinkedList.insert_after(50,55)
myLinkedList.print_list()
print("")
result = myLinkedList.search(50)
print("Search result is  : ",result.item)
# print("")
myLinkedList.print_list()
print("")
print("List is Empty :  : ",myLinkedList.is_empty())
myLinkedList.delete_first()
print("My List After Deleted first Node")
myLinkedList.print_list()
print("")
myLinkedList.delete_last()
myLinkedList.delete_last()
print("My List After Deleted Last Node")
myLinkedList.print_list()
print("")
myLinkedList.delete_item(55)
myLinkedList.delete_item(20)
print("My List After Deleted specific  Node")
myLinkedList.print_list()

print("")
print("Print using Itarator")
for i in myLinkedList:
    print(i,end=" ")