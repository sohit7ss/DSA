# divive and merge algorithm 
# 
# # Merge Sort is an efficient sorting algorithm based on the Divide and Conquer technique.
# It divides the array into smaller subarrays, sorts them, and then merges them back together to produce the final sorted array.
# 1️⃣ Technique Used
# Merge Sort works using the Divide and Conquer strategy.
# Three main steps:
# Divide – Split the array into two halves.
# Conquer – Recursively sort each half.
# Merge – Combine the sorted halves into a single sorted array.
# 2️⃣ Example
# Unsorted array:
# [38, 27, 43, 3, 9, 82, 10]
# Step 1: Divide
# [38,27,43,3,9,82,10]
#         ↓
# [38,27,43]   [3,9,82,10]
# Divide again:
# [38] [27] [43]   [3] [9] [82] [10]
# Step 2: Merge Sorted Parts
# Merge step-by-step:
# [38] [27] → [27,38]
# [27,38] [43] → [27,38,43]
# [3] [9] → [3,9]
# [82] [10] → [10,82]
# [3,9] [10,82] → [3,9,10,82]
# Final merge:
# [27,38,43] + [3,9,10,82]
# → [3,9,10,27,38,43,82]



a = [1, 2, 3, 4]
b = [1, 5, 6, 7, 8, 9]
nums = [6, 7, 9, 3, 4, 2, 1]


def merge_two(left, right):
    result = []
    i,j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    if i < n:
        while i < n:
            result.append(left[i])
            i +=1
    if j < m:
        while j < m:
            result.append(right[j])
            j +=1
    return result

def merge_sort(arr):
    mid = len(arr)//2
    if len(arr) == 1:
        return arr
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_two(left_half, right_half)



print(merge_two(a,b))
print(merge_sort(nums))

# here time complexity is 
#  we devided by 2 so time complexity is log2(n)
# and we done for all n array
# so overall time peroid is O(n log2(n))

# SC = O(n)
