class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def print(self):
        cur = self.value
        if cur != None:
            print(cur)
            cur = self.left_child
            cur.print()
            

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_child = BinaryTree(value)
            new_child.left_child = self.left_child
            self.left_child = new_child

b = BinaryTree(1)
b.insert_left(2)
b.insert_left(3)
b.insert_left(4)
b.print()