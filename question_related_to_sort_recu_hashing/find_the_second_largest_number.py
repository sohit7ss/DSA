nums = [55, 32, -57, -55, 45, 62, -67, 99]

# brute force solution

nums.sort()
print(nums[-2])

# better solution
def second_largest(nums):
    largest = float("-inf")
    smallest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        largest = max ( largest , nums[i])
    for i in range(0,n):
        if nums[i]> smallest and nums[i] != largest:
            smallest = nums[i]
    return smallest

print(second_largest(nums))

# best solution 
# better solution
def second_largest1(nums):
    largest = float("-inf")
    smallest = float("-inf")
    n = len(nums)

    for i in range(0,n):
        if nums[i] > largest :
            smallest = largest
            largest = nums [i]
        elif nums[i] > smallest and nums[i] != largest:
            smallest = nums[i]

    return smallest

print(second_largest1(nums))