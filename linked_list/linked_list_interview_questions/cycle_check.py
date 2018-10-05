class Node(object):
    def __init__(self, head):
        self.head = head
        self.nextnode = None

def isCycled(node:Node):
    pointer_1 = node
    pointer_2 = node

    while pointer_2 != None and pointer_2.nextnode != None:
        pointer_1 = pointer_1.nextnode
        pointer_2 = pointer_2.nextnode.nextnode
        if pointer_1 == pointer_2:
            return True
    return False



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = a

print(isCycled(a))