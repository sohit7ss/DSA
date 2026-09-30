def binary_search(nums, low, high,target):
    if low>high: return -1
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid]< target:
        return binary_search(nums, mid + 1, high, target)
    else:
        return binary_search(nums, low, mid - 1, target)



nums = [3, 4, 5, 6, 7, 8, 9, 39, 40, 44, 45, 46 ]

target = 5

print(binary_search(nums,0, len(nums), target))