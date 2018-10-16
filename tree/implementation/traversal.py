class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
    
    def insert_left(self, val):
        if self.leftChild == None:
            self.leftChild = BinaryTree(val)
        else:
            new_tree = BinaryTree(val)
            new_tree.leftChild = self.leftChild
            self.leftChild = new_tree
    
    def insert_right(self, val):
        if self.rightChild == None:
            self.rightChild = BinaryTree(val)
        else:
            new_tree = BinaryTree(val)
            new_tree.rightChild = self.rightChild
            self.rightChild = new_tree

    def getLeftChild(self):
        return self.leftChild
        
    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.getLeftChild().preorder()
        if self.rightChild:
            self.getRightChild().preorder()

r = BinaryTree(1)
r.insert_left(2)
r.insert_right(5)
r.insert_left(4)
r.insert_right(3)
r.insert_left(6)
r.preorder()