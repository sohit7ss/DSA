from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        result = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        # while len(neg) > 0:
        #     p = pos.pop()
        #     n = neg.pop()
        #     result.append(p)
        #     result.append(n)
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result


class Solution:
    def rearrangeArrayOptimal(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos_index, neg_index = 0, 1
        for i in range(0,n):
            if nums[i]>=0 :
                result[pos_index] = nums[i]
                pos_index += 2
            else:
                result[neg_index] = nums[i]
                neg_index += 2
        return result