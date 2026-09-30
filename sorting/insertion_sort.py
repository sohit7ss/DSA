# Insertion Sort
# Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted array one element at a time by inserting each element into its correct position in the already sorted part of the list.
# The idea is similar to arranging playing cards in your hand.
# 🔹 Basic Idea
# The array is divided into two parts:
# Sorted part (left side)
# Unsorted part (right side)
# At each step:
# Take one element from the unsorted part.
# Insert it into the correct position in the sorted part.

# 🔹 Example
# Unsorted array:
# [8, 3, 5, 2, 9]

#   Pass 1
# Compare 3 with 8
#  Insert before 8
# [3, 8, 5, 2, 9]

# Pass 2
# Insert 5 in correct position
# [3, 5, 8, 2, 9]

# Pass 3
# Insert 2 at correct position
# [2, 3, 5, 8, 9]

# Pass 4
# Insert 9 (already in correct position)
# Final sorted array:
# [2, 3, 5, 8, 9]

# 🔹 Technique Used
# Insertion Sort works on:
# Comparison Technique Elements are compared with previous elements.

# Insertion Technique
# Each element is inserted into its correct position.

# Internal Sorting
# Data is stored in main memory.

# 🔹 Algorithm

nums = [6, 7, 9, 3, 4, 2, 1]
def insertion_sort(nums):
    l = len(nums)
    for i in range(0 , l-1):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -=1
        nums[j+1] = key 

    return nums

print(insertion_sort(nums))


# here time complexity 
#       1 + 2 + ..... + n
#       + n for while loop
# so TC = (n^2)
# and SC = (n^2)