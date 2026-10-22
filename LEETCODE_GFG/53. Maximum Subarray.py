from typing import List
nums = [49,-64,94,18,11,48,16,2,-26,47,99,-21,-50,55,-23,-94,-73,46,-85]



def maxSubArray(nums):
        summ = 0
        max_sum = nums[0]
        # i = 0
        # j = len(nums)
        # while i<j:
        #     summ = sum(nums[i:j])
        #     i += 1
        #     max_sum = max(max_sum, summ)
        
        # while j>0:
        #     summ = sum(nums[0:j])
        #     j -= 1
        #     max_sum = max(max_sum, summ)
        for i in range(len(nums)):
                for j in range(i + 1, len(nums) + 1):
                        summ = sum(nums[i:j])
                        max_sum = max(max_sum, summ)
        max_sum = max(max_sum, summ)
        return max_sum

# print(maxSubArray(nums))



def maxSubArrayOptimal(nums):
        maxi = nums[0]
        total = 0
        
        for i in range(0,len(nums)):
                total += nums[i]
                maxi = max(maxi, total)
                if total < 0:
                        total = 0
        return maxi

print(maxSubArrayOptimal(nums))