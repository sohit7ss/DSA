class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(current.copy())
                return

            # Include nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)

            # Don't include nums[i]
            current.pop()
            backtrack(i + 1, current)

        backtrack(0, [])

        return result