class BSTNode:

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self,val):
        if not self.val:
            self.val = val
            return
        
        if self.val == val:
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)

        if self.left is not None:
            self.left.preorder(vals)

        if self.right is not None:
            self.right.preorder(vals)

        return vals

    def innorder(self, vals):
        if self.left is not None:
            self.left.innorder(vals)

        if self.val is not None:
            vals.append(self.val)

        if self.right is not None:
            self.right.innorder(vals)

        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)

        if self.right is not None:
            self.right.postorder(vals)

        if self.val is not None:
            vals.append(self.val)

        return vals

    def getMin(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def getMax(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def find(self, val):
        if val == self.val:
            return True
        
        if val < self.val:
            if self.left == None:
                return False
            return self.left.find(val)

        if val > self.val:
            if self.right == None:
                return False
            return self.right.find(val)

    def delete(self, val):
        if self == None:
            return self
        
        if self.right == None:
            return self.left

        if self.left == None:
            return self.right

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        min_larger_node = self.right

        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
    
def main():

    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()

    for num in nums:
        bst.insert(num)

    print("------MIN--------")
    print(bst.getMin())
    print(" ")

    print("------MAX--------")
    print(bst.getMax())
    print(" ")

    print("------FIND 24--------")
    print(bst.find(24))
    print(" ")

    print("------PREORDER--------")
    print(bst.preorder([]))
    print(" ")

    print("------INNORDER--------")
    print(bst.innorder([]))
    print(" ")

    print("------POSTORDER--------")
    print(bst.postorder([]))
    print(" ")

    nums = [2, 6, 20] #### DUDA

    print(f"--- DELETING... {str(nums)} ------")

    for num in nums:
        bst.delete(num)

    print("") 

    print("------NEW INNORDER--------")
    print(bst.innorder([]))
    print(" ")

main()