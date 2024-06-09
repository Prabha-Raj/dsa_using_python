class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Dll:
    def __init__(self,start=None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        newNode = Node(prev=None,item=data,next=self.start)
        if not self.is_empty():
            self.start.prev = newNode
        self.start = newNode

    def insert_at_end(self,data):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                if tempNode.next is None:
                    tempNode.next = Node(prev=tempNode,item=data,next=None)
                    break
                tempNode = tempNode.next
        else:
            newNode = Node(item=data)
            self.start= newNode
    
    def search(self,data):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                if tempNode.item is data:
                    return tempNode
                tempNode = tempNode.next
            return None
    def insert_after(self,temp,data):
        if not self.is_empty():
            if temp is not None:
                newNode = Node(prev=temp,item=data,next=temp.next)
                if temp.next is not None:
                    temp.next.prev=newNode
                temp.next = newNode
    def print_list(self):
        tempNode = self.start
        while tempNode is not None:
            print(tempNode.item,end=" ")
            tempNode = tempNode.next
    
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if not self.is_empty():
            pass
        elif self.start.next is not None:
            self.start = None
        else:
            tempNode = self.start
            while tempNode.next is not None:
                tempNode = tempNode.next
            tempNode.prev.next = None
    
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            tempNode = self.start
            while tempNode is not None:
                if tempNode.item is data:
                    if tempNode.next is not None:
                        tempNode.next.prev = tempNode.prev
                    if tempNode.prev is not None:
                        tempNode.prev.next = tempNode.next
                    else:
                        self.start = tempNode.next
                    break
                tempNode = tempNode.next

    def __iter__(self):
        return DllIterator(self.start)

class DllIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data




# myDLinkedList = Dll()
# # print(myDLinkedList.is_empty())
# myDLinkedList.insert_at_start(10)
# myDLinkedList.insert_at_end(20)
# myDLinkedList.insert_after(myDLinkedList.search(10),15)
# # print(myDLinkedList.is_empty())
# myDLinkedList.print_list()

# print("\nprint using  Itarator class")
# for x in myDLinkedList:
#     print(x)

    