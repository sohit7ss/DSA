from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        if n < 4:
            return []
        my_set = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l ]== target:
                            my_set.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))

        return [list(x) for x in my_set]

# TC = O(N^4)
# SC = O(no. of triplate)


class Solution:
    def fourSum_brute(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                my_set = set()

                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in my_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        result.add(tuple(temp))

                    my_set.add(nums[k])

        return [list(ans) for ans in result]


# TC = O(N^3)
# SC = O(no. of triplate) + O(n)


class Solution:
    def fourSum_optimal(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        ans = []

        nums.sort()

        for i in range(n - 3):

            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:

                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])

                        k += 1
                        l -= 1

                        # Skip duplicate k
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        # Skip duplicate l
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif total < target:
                        k += 1

                    else:
                        l -= 1

        return ans


# TC = O(N^3)
# SC = O(no. of ans) 
