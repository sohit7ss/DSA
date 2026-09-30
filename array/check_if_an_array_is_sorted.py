class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        
        if len(arr) == 1:
            return True
             
        for i in range( 0, (len(arr)-2)):
            if arr[i]>arr[i+1]:
                return False
        return True
        
                
        # TC = O(N)
    #     SC = O(1)