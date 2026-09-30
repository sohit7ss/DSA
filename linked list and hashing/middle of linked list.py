class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_linked_list:
    def __init__(self):
        self.head = None

    def append (self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node


# here time complexity is TC = O(N) (in worst case)
# and its space complexity is SC = O(1)                         -------> this is for append

    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val , end = "  ")
                curr = curr.next

# here time complexity is TC = O(N) (in worst case)
# and its space complexity is SC = O(1)                         -------> this is for traversal


# insert at specific position
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while count is not None and count<position:
                prev_node = curr
                curr = curr.next
                count += 1
            prev_node.next = new_node
            new_node.next = curr

# here time complexity is TC = O(N) (in worst case)
# and its space complexity is SC = O(1)                         -------> this is for insert at any position



# detete node
    def delete (self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")
    # middle of the linked list 
    # def middle(self):
    #     n = 0
    #     temp = self.head
    #     while temp.next is not None:
    #         n += 1
    #         temp = temp.next
    #     if n % 2 == 0:
    #         m = n//2
    #     else:
    #         m = n//2 + 1
    #     count = 0
    #     temp1 = self.head
    #     while count < m:
    #         count +=1
    #         temp1 = temp1.next
    #     print("\n the middel node is ",temp1.val)

    def middle(self):
        if self.head is None:
            return None

        # count nodes
        n = 0
        temp = self.head
        while temp:
            n += 1
            temp = temp.next

        # find middle index
        m = n // 2

        temp = self.head
        for _ in range(m):
            temp = temp.next
        # for i in range (m ,n):
        #     print("\nMiddle node is:", temp.val)
        #     temp = temp.next




sll = Singly_linked_list()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(80)
sll.insert_at(60, 3)
sll.delete(20)
sll.delete(90)
sll.traversal()
sll.middle()




