nums = [10, 301,332,211,21, -1, -323, -44,-22, 32, 43, -234, 3234]

def linear_search(target_nums: int, nums: list[int]) -> int | str:
    for i in range(0, len(nums)):
        if nums[i] == target_nums:
            return target_nums
    
    return "nums not available"

print(linear_search(-331, nums))
        