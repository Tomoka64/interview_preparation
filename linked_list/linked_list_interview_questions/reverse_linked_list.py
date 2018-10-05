class Node(object): 
    def __init__(self,head):
        self.head = head
        self.nextnode = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, node):
        new_node = Node(node)
        if self.head == None:
            self.head = new_node
            return
        cur = self.head
        while cur.nextnode:
            cur = cur.nextnode
        cur.nextnode = new_node
    
    def println(self):
        cur = self.head
        while cur:
            print(cur.head)
            cur = cur.nextnode

    def reverse(self): 
        prev = None
        current = self.head 
        while current: 
            next = current.nextnode
            current.nextnode = prev 
            prev = current 
            current = next
        self.head = prev 

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.reverse()
l.println()
