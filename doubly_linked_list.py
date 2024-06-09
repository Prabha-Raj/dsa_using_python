class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.item = data
        self.next = next

class DoublyLinkedList:
    def __init__(self,start=None):
        self.start =start
    
    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False
    
    def insert_at_first(self,data):
        newNode = Node(prev=None,data=data,next=self.start)
        if not self.is_empty():
            self.start.prev = newNode
        self.start=newNode
        
    def insert_at_last(self,data):
        if self.start is None:
            newNode = Node(None,data,self.start)
            self.start=newNode
        else:
            tempNode = self.start
            while tempNode is not None:
                if tempNode.next is None:
                    newNode = Node(tempNode,data,None)
                    tempNode.next = newNode
                    break
                tempNode=tempNode.next
    
    def insert_after(self,item,data):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                if tempNode.item is item:
                    newNode = Node(tempNode,data,tempNode.next)
                    tempNode.next = newNode
                    break
                tempNode = tempNode.next

    def delete_first(self):
        if not self.is_empty():
            self.start=self.start.next

    def delete_last(self):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                if tempNode.next.next is None:
                    tempNode.next = None
                    break
                tempNode = tempNode.next
    def delete_item(self,data):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                if tempNode.item is data and tempNode.prev is None:
                    self.start = tempNode.next
                    self.start.prev = None
                    break
                elif tempNode.next.item is data and tempNode.next.next is None:
                    if tempNode.next.next is None:
                        tempNode.next = None
                        break
                    break
                elif tempNode.item is data:
                    tempNode.prev.next = tempNode.next 
                    tempNode.next.prev = tempNode.prev
                    break
                tempNode = tempNode.next

    def print_list(self):
        if not self.is_empty():
            tempNode = self.start
            while tempNode is not None:
                print(tempNode.item,end=" ")
                tempNode = tempNode.next
    def search(self,data):
        if self.start is not None:
            tempNode = self.start
            while tempNode is not None:
                if tempNode.item is data:
                    return tempNode
                tempNode = tempNode.next    
            return None
                

# creating instance object of DoublyLinkedList class
myList = DoublyLinkedList()

# inserting alement in list at first
myList.insert_at_first(35)
myList.insert_at_first(30)
myList.insert_at_first(25)
myList.insert_at_first(20)
myList.insert_at_first(15)
myList.insert_at_first(10)
print("\nMy List after inseting element by using insert_at_last Function :")
myList.print_list()

# inserting alement in list at last
myList.insert_at_last(40)
myList.insert_at_last(44)
myList.insert_at_last(48)
myList.insert_at_last(50)
myList.insert_at_last(54)
myList.insert_at_last(58)
myList.insert_at_last(60)
print("\nMy List after inseting element by using insert_at_last Function :")
myList.print_list()


# inserting alement in list after some element
myList.insert_after(40,45)
print("\nMy List after inseting element by using insert_after Function :")
myList.print_list()


# deleting first element  in list  
myList.delete_first()
print("\nMy List after deleting first element by using delete_first Function :")
myList.print_list()




# deleting last element  in list  
myList.delete_last()
print("\nMy List after deleting last element by using delete_last Function :")
myList.print_list()


# deleting specified element  in list  
# myList.delete_item(20)
# myList.delete_item(35)
# myList.delete_item(50)
print("\nMy List after deleting specified element by using delete_item Function :")
myList.print_list()
print("\nsearch item  result :", myList.search(15))