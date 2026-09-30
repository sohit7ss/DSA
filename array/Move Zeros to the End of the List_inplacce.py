def moveZeroes_brute(nums):
        n = len(nums)
        temp = []
        for i in range (0,n):
            if nums[i] != 0:
                temp.append(nums[i])

        n2 = len(temp)
        for i in range(0,n2):
            nums[i] = temp[i]
        for i in range(n2,n):
            nums[i] = 0
        return nums

# TC = O(2n)
# SC = O(n)

nums = [2, 4, 0, 9, 5, 2, 0, 4, 3, 5, 0, 0, 2]

def moveZeroes_optimal(nums):
    if len(nums) == 1:
        return
    i = 0
    while i<len(nums):
        if nums[i] == 0:
            break
        i +=1
    if i == len(nums):
        return
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i] , nums[j] = nums[j] , nums[i]
            i +=1
        j +=1
    


def moveZero_optimal_2(nums):
        n = len(nums)
        m = len(nums)-1
        while n > 0:
            if nums[n-1] == 0:
                for i in range(n-1, m):
                    nums[i] , nums[i+1] = nums[i+1], nums[i]
                m = m-1
            n = n-1
        return nums


def moveZero_optimal_3(nums):
        for i in nums:
            if(i==0):
                nums.remove(0)
                nums.append(0)
                    