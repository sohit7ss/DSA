class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
        self.prev = None

n1 = Node(12)
n2 = Node(23)
n3 = Node(24)

n1.next = n2
n2.next = n3
n3.prev = n2
n2.prev = n1

print(n1.val)