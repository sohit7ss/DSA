class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Double_inked_list:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
# TC = O(N)
# SC = O(1)

    def add_at_the_last(self, val):
        new_node = Node(val)
        temp = self.head
        if not self.head:
            self.head = new_node        
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
# TC = O(N)
# SC = O(1)

    def insert_in_between(self, position, val):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
        
        temp = self.head
        count = 0
        while temp and count < position - 1:  # --------> remember
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of bound")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next :
            temp.next.prev = new_node
        temp.next = new_node
# TC = O(N)
# SC = O(1)

    def traverse_forward(self):
        if self.head is None:
            print("Empty")
            return        
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        
# TC = O(N)
# SC = O(1)

    def traverse_backward(self):
        if self.head is None:
            print("Empty")
            return        
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.val, end=" ")
            temp = temp.prev
        
# TC = O(N)
# SC = O(1)

    def delete_head(self):
        self.head = self.head.next
# TC = O(1)
# SC = O(1)

    def delete_last(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
# TC = O(N)
# SC = O(1)
    def delete_in_between(self, val):
        temp = self.head

        if temp is None:
            return

        # Case 1: delete head
        if temp.val == val:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return
                                                                    # ----------------> do again
        # Traverse
        while temp is not None:
            if temp.val == val:
                # Case 2: middle or last node
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                return
            temp = temp.next

        print("Node not found")
    
    def reverse_a_doubley_linked_list_brute(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp = self.head
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        return self.head
# TC = O(2N)
# SC = O(N)
    def reverse_a_doubley_linked_list_optimal1(self):
        temp = self.head
        prev_node = None

        while temp:
            # Swap next and prev
            temp.prev, temp.next = temp.next, temp.prev
            
            prev_node = temp
            temp = temp.prev  # move using swapped pointer

        if prev_node:
            self.head = prev_node

        return self.head
    
    # def reverse_a_doubley_linked_list_optimal2(self):
    #     temp = self.head
    #     prev_node = None
    #     front = self.head.next

    #     while front:

    def delete_all_occurences_of_key(self, key):
        temp = self.head
        if self.head.next is None and self.head == key:
            return None

        while temp:
            next_node = temp.next  # store next node

            if temp.val == key:

                # Case 1: Head node
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                # Case 2: Middle or Tail
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev

            temp = next_node

        return self.head
    
    def findPairsWithGivenSum_brute(self, target):
        
        key = self.head
        result = []
        while key:
            if key is None:
                break
            temp = key.next
            while temp:
                if (temp.val + key.val==target):
                    result.append((key.val, temp.val))
                temp = temp.next
            key = key.next
        return result
    # here time complexity is O(n(n+1)/2) == O(n^2)

    def findPairsWithGivenSum_better(self, target):
        temp = self.head
        
        empty_set = set()
        result = []
        while temp:
            key = target-temp.val
            if key in empty_set:
                result.append((key, temp.val))
            empty_set.add(temp.val)
            temp = temp.next
        return result
# this work but this not give the result in sorted manner cuz it take the value in so if target is 7 then in first iteration key is 6(7-1) so it check 6 is set but in set 
# 6 is not available so it goes to next when the 6 is added it check 1 and that time 1 is in the set but berfor this (2,5) is already added

# TC = O(N)
#  SC = O(N)

    def findPairsWithGivenSum_optimal(self, target):
        left = self.head
        right = self.head
        result = []

        while right.next:
            right = right.next
        
        while left!=right and right.next != left:
            if left.val + right.val == target:
                result.append((left.val, right.val))
                left = left.next 
                right = right.prev
            elif left.val + right.val < target:
                left = left.next
            else:
                right = right.prev
        return result

# 

# Initialize two pointers: left at head and right at the last node.
# At each step, compute sum = left.data + right.data.
# If sum equals target → store pair and move both pointers inward.
# If sum is smaller → move left forward; if larger → move right backward.
# Stop when pointers meet or cross to avoid duplicates and extra checks.
# Time: O(n)+O(n) == O(n)
# Space: O(1)

    def RemoveDuplicatesFromSortedDLL(self):
        # left = self.head
        # right = self.head.next
        # while left and right:
        #     if left.val == right.val:
        #         while left.val == right.val:                  -------> not correct logic 
        #             right = right.next
        #         left.next = right
        #         right.next = left
        #     right = right.next
        #     left = left.next
        # return self.head
        curr = self.head.next 
        while curr:
            if curr.prev.val == curr.val:
                if curr.prev == self.head:
                    curr.prev = None
                    self.head = curr
                else:
                    curr.prev.prev.next = curr
                    curr.prev = curr.prev.prev
            curr = curr.next
        return self.head
    



    









dll = Double_inked_list()
dll.insert_at_head(12)
dll.insert_at_head(10)
dll.add_at_the_last(33)
dll.insert_at_head(22)
dll.insert_in_between(3,29)
dll.traverse_forward()
print("\n")
dll.traverse_backward()
print("\n")
dll.delete_head()
dll.traverse_forward()
print("\n")
dll.insert_at_head(55)
dll.delete_last()
dll.traverse_forward()
dll.reverse_a_doubley_linked_list_brute()
print('\n')
dll.traverse_forward()
dll.reverse_a_doubley_linked_list_optimal1()
print('\n')
dll.insert_at_head(10)
dll.insert_in_between(3,10)
dll.traverse_forward()
print('\n')
dll.delete_all_occurences_of_key(10)
dll.traverse_forward()
dll.delete_all_occurences_of_key(55)
dll.delete_all_occurences_of_key(12)
dll.delete_all_occurences_of_key(29)
dll.insert_at_head(40)
dll.insert_at_head(30)
dll.insert_at_head(24)
dll.insert_at_head(7)
dll.insert_at_head(6)
dll.insert_at_head(5)
dll.insert_at_head(2)
dll.insert_at_head(1)
print("\n")
dll.traverse_forward()
print("\n")
print(dll.findPairsWithGivenSum_brute(7))
print("\n")
dll.traverse_forward()
print("\n")
print(dll.findPairsWithGivenSum_better(7))
print("\n")
dll.traverse_forward()
print("\n")
print(dll.findPairsWithGivenSum_optimal(7))
dll.insert_in_between(2,2)
dll.insert_in_between(2,2)
dll.insert_in_between(5,5)
dll.traverse_forward()
print("\n")
dll.RemoveDuplicatesFromSortedDLL()
dll.traverse_forward()
