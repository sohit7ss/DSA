nums = [1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 6, 9, 9, 9, 10]

def remove_duplicate_brute(nums):
    n = len(nums)
    freq_dict = {}
    for i in range (0,n):
        freq_dict[nums[i]] = 0
    j= 0
    for k in freq_dict:
        nums[j] = k
        j +=1
    return j

# TC = O(2N) == O(N)\
# SC = O(N)

def remove_duplicate_optimal(nums):
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        j = i + 1
        while j< n:
            if nums[i] != nums[j]:
                i =i + 1
                nums[i] , nums[j] = nums[j], nums[i]
            j +=1
        return i + 1

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 1
#         i = 0
        
#         for j in range (0,n):
#             if nums[i] != nums[j]:
#                 i =i + 1
#                 nums[i] , nums[j] = nums[j], nums[i]
#         return i+1

#  TC = O(N)
#  SC = O(1)