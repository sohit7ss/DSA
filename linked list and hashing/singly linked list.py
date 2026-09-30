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

    # middle term of the linked list
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    # this is known as tortoise-hare method 
    # and its time complexity is TC = O(N/2)
    # and its space complexity is SC = O(1)

    def reverse_sll_brute(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        temp = self.head
        while temp:
            e = stack.pop()
            temp.val = e
            temp = temp.next
        return self.head
    # here time complexity is for while loop so the time complexity is TC = O(N + N)
    # and space complexity is for we create a stack and then pop. SC = O(N)


    def reverse_sll_optimal(self):
        temp = self.head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    # here time complexity is TC = O(N)
    # and its space complexity is SC = O(1)

    def cycle_check_brute(self):
        my_set = set()
        temp = self.head
        while temp:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
        return False
    # here time complexity is TC = O(N)
    # and its space complexity is SC = O(N)
     
    def cycle_check_optimal(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    # here time complexity is TC = O(N)
    # and its space complexity is SC = O(1)
            

    def cycle_node_start_brute(self):
        my_set = set()
        temp = self.head
        while temp:
            if temp in my_set:
                return True
            temp = temp.next
        return False
    # this is a brute force method to find the starting node of cycle list in singly linked list and its time compexity is TC = O(N);
    # and its spcae complexity is SC = O(N)

    def cycle_node_star_optimal(self):   # -----> this is for finding the starting node of where the cycle start
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            
    #This is the 🔁 Floyd’s Cycle Detection Algorithm, also known as the:

    # 👉 Tortoise and Hare Algorithm
    # here time complexity is TC = O(N)
    # and its space complexity is SC = O(1)

    def length_of_cycle_brute (self):
        my_dict = dict()
        temp = self.head
        travel = 0
        while temp:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
        return 0
    # here time complexity is TC = O(N)
    # and its space complexity is SC = O(N)    

    def length_of_cycle_optimal (self):
        slow = self.head
        fast = self.head

        # Step 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: count cycle length
                count = 1
                temp = slow.next

                while temp != slow:
                    temp = temp.next
                    count += 1

                return count

        return 0  # no cycle
    # here time complexity is TC = O(N)
    # and its space complexity is SC = O(1)
    
    # this is known as Floyd's algorithm.

    # odd even linked list in ssl 
    def odd_even_linked_list_brute (self):
        # value = []
        # temp = self.head
        # while temp:
        #     value.append(temp.val)
        #     temp = temp.next.next
        # temp = self.head.next
        # while temp:
        #     value.append(temp.val)
        #     temp = temp.next.next
        # return value
        value = []
        
        # Odd index nodes
        temp = self.head
        # while temp and temp.next:
        #     value.append(temp.val)
        #     temp = temp.next.next

        # temp = self.head.next
        # while temp and temp.next:
        #     value.append(temp.val)
        #     temp = temp.next.next

        while temp:
            value.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Even index nodes
        temp = self.head.next if self.head else None
        while temp:
            value.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        temp = self.head
        index = 0
        while temp:
            temp.val = value[index]
            index += 1
            temp = temp.next


        return self.head
        # here time complexity is TC = O(N/2 + N/2 + N)
        # and its space complexity is SC = O(1)

    def odd_even_linked_list_optimal(self):
        if self.head is None:
            return None

        if self.head.next is None:
            return self.head
        odd  = self.head
        even = self.head.next
        even_head = self.head.next

        # while odd and odd.next:
        #     odd.next = odd.next.next
        #     odd = odd.next                    ------> this is not a way to do this. cuz when we do seprate even and odd then the linked list change in odd then it broke and totally fucked up
        # while even and even.next:
        #     even.next = even.next.next
        #     even = even.next

        while even and even.next:
            odd.next = even.next
            # odd = odd.next.next               ----> here we already shift odd.next
            odd = odd.next
            even.next = odd.next
            # even = even.next.next             -----> same here
            even = even.next
            

        odd.next = even_head

        return self.head
        # here time complexity is TC = O(N/2)
        # and its space complexity is SC = O(1)

    #
    # 
    # 
    # remove N th node form the last
    def remove_N_th_node_from_last_brute(self,n):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        if n<count:
            m= count- n
            temp = self.head
            c = 0
            while c != m-1:
                temp = temp.next
                c += 1
            if temp.next:
                temp.next = temp.next.next
        elif n == count:
            self.head = self.head.next
        else:
            print("value out of range")
        return self.head
        # here time complexity is TC = O(N + N)
        # and its space complexity is SC = O(N + N)

    def remove_N_th_node_from_last_optimal(self,n):
        slow = self.head
        fast = self.head
        for _ in range (n):
            fast = fast.next
        if fast == None:
            return self.head.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return self.head
        # here time complexity is TC = O(N)
        # and its space complexity is SC = O(1)    




sll = Singly_linked_list()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.insert_at(60, 3)
sll.traversal()
sll.delete(20)
sll.delete(90)
sll.traversal()
print(sll.reverse_sll_brute())
print(sll.cycle_check_brute())
print(sll.cycle_check_optimal())
sll.traversal()
sll.odd_even_linked_list_brute()
print("\n")
sll.traversal()
sll.odd_even_linked_list_optimal()
print("\n")
sll.traversal()
print("\n")
sll.remove_N_th_node_from_last_brute(2)
sll.traversal()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
print("\n")
sll.traversal()
sll.remove_N_th_node_from_last_optimal(4)
print("\n")
sll.traversal()
