# Selection Sort is a simple comparison-based sorting algorithm that repeatedly selects the minimum (or maximum) element from the unsorted portion and places it at its correct position.
# It divides the array into two parts:
# Sorted part (left side)
# Unsorted part (right side)
# At each iteration:
    # Find the smallest element in the unsorted portion.
    # Swap it with the first element of the unsorted portion.
    # Move the boundary of the sorted portion one step right.

# Step-by-Step Example
# Unsorted array:
# [64, 25, 12, 22, 11]

# Pass 1:
# Smallest = 11
# Swap with first element (64)
# [11, 25, 12, 22, 64]

# Pass 2:
# Smallest (from index 1 to end) = 12
# Swap with 25
# [11, 12, 25, 22, 64]

# Pass 3:
# Smallest = 22
# Swap with 25
# [11, 12, 22, 25, 64]
 
# Pass 4:
# Smallest = 25
# Already in correct place
# Final Sorted Array:
# [11, 12, 22, 25, 64]



# Selection Sort belongs to comparison-based sorting algorithms



# Alogoritm

nums = [6, 7, 9, 3, 4, 2, 1]

def selection_sorting (nums):
    n = len(nums)
    
    for i in range (0, n-1):
        min_num_ind = i
        for j in range (i+1, n):
            if nums[j] < nums [min_num_ind]:
                min_num_ind = j
        nums[i], nums[min_num_ind] = nums[min_num_ind], nums[i]
    return nums

print(selection_sorting(nums))

# here time complexity is O(N^2)
# here in first pass time complexity = n
# in second pass = n-1
# ....
# in last pass = 1
# so 1 + 2 + 3 + ..... + n = n(n+1)/2 = O(n^2)
#
# SC = O(1)