head = [1,2,3,4,5]
class Solution:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.head = None
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
