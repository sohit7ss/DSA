'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.

    def deleteAllOccurOfX(self, head, x):
        temp = head
        
        while temp:
            next_node = temp.next   # store next
            
            if temp.data == x:
                # If node is head
                if temp.prev is None:
                    head = temp.next
                    if head:
                        head.prev = None
                
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
            
            temp = next_node
        
        return head