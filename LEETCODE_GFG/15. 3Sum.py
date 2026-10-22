

class Solution:
    def threeSum_brute(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        my_set = set()
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        my_set.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(x) for x in my_set]

# TC = O(N^3)
# SC = O(no. of triplate)


class Solution:
    def threeSum_brute2(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        my_set = set()
        for i in range(n-2):
            for j in range(i+1,n-1):
                if -(nums[i] + nums[j]) in nums[j+1:n]:
                    my_set.add(tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])])))
        return [list(x) for x in my_set]


# TC = O(N^3)
# SC = O(no. of triplate)


class Solution:
    def threeSum_better(self, nums: list[int]) -> list[list[int]]:

        result = set()
        n = len(nums)

        for i in range(n):
            my_set = set()

            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])

                if third in my_set:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))

                my_set.add(nums[j])

        return [list(ans) for ans in result]


# TC = O(N^2)
# SC = O(no. of triplate) + O(n)



class Solution:
    def threeSum_optimal(self, nums: list[int]) -> list[list[int]]:

        ans = []
        n = len(nums)
        nums.sort()
        for i in range(0,n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum > 0:
                    k -= 1
                elif total_sum < 0:
                    j += 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1

                    # skip the duplicates if occured
                    while j < k  and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


# TC = O(N^2) + O(n log n)
# SC = O(no. of triplate) 