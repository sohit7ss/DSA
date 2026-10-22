from typing import List

class Solution:
    def longestConsecutive_brute(self, nums: List[int]) -> int:
        max_count = 0
        

        for i in range(0, len(nums)):
            num = nums[i]
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1
            max_count = max(max_count, count)
        return max_count

class Solution:
    def longestConsecutive_best(self, nums: List[int]) -> int:
        maxx = 0
        count = 0
        if len(nums) == 0:
            return 0

        for i in range(min(nums), max(nums)+1, 1):
            
            if i in nums:
                count += 1
                maxx = max(count, maxx)

            else:
                count = 0
        return maxx


class Solution:
    def longestConsecutive_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set()
        for i in range(0,n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num - 1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                if count > longest:
                    longest = count
        return longest


