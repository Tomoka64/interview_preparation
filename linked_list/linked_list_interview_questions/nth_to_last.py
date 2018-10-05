class Node:
    def __init__(self, head):
        self.head = head
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def println(self):
        cur = self.head
        while cur:
            print(cur.head)
            cur = cur.next
        
    def nth_to_last(self, n):
        counter = 0
        cur = self.head
        follower = self.head
        while counter < n:
            cur = cur.next
            counter += 1
        while cur.next:
            cur = cur.next
            follower = follower.next
        return follower.head

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l.nth_to_last(2))

