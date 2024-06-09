class Node:
    def __init__(self,item=None,left=None,right=None):
        self.left = left
        self.item = item
        self.right = right
class BST:
    def __init__(self):
        self.root = None        

    def insert(self,data):
        self.root = self.r_insert(self.root,data)
    def r_insert(self,root,data):
        if root is None:
            return Node(item=data)
        if data < root.item :
            root.left = self.r_insert(self.left,data)
        elif data > root.item:
            root.right = self.r_insert(root.right,data)
        return root
    def search(self,data):
        return self.r_search(self.root,data)
    def r_search(self,root,data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.r_search(root.left,data)
        elif data > root.right:
            return self.r_search(root.right,data)
    
    def in_order(self):
        result = []
        self.r_in_order(self.root,result)
        return result
    def r_in_order(self,root,result):
        if root:
            self.r_in_order(self.left,result)
            result.append(root.item)
            self.r_in_order(root.right,result)

    def pre_order(self):
        result = []
        self.r_in_order(self.root,result)
        return result
    def r_pre_order(self,root,result):
        if root:
            result.append(root.item)
            self.r_pre_order(self.left,result)
            self.r_pre_order(root.right,result)
  
    def post_order(self):
        result = []
        self.r_post_order(self.root,result)
        return result
    def r_post_order(self,root,result):
        if root:
            self.r_post_order(self.left,result)
            self.r_post_order(root.right,result)
            result.append(root.item)

    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def max_value(self,temp):
        current = item
        while current.right is not None:
            current = current.right
        return curren.item
    
    def delete(self,data):
        self.root = r_delete(self.root,data)
    
    def r_delete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.r_delete(root.left, data)
        elif data > root.item:
            root.right = self.r_delete(root.right, data)
        elif data == root.item:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.item = self.min_value(root.right)
                self.r_delete(root.right, root.item)
        return root
    def size(self):
        return len(self.in_order())

bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(40)
bst.insert(50)
bst.insert(60)
bst.insert(70)
bst.insert(80)
bst.insert(90)
bst.insert(100)
# result = bst.in_order()
# if result:
#     for i in result:
#         print(i,end=" ")
















