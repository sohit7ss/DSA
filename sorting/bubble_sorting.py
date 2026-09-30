# Bubble Sort
# Bubble Sort is a simple comparison-based sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# It works by “pushing” the largest element to the end in each pass — just like bubbles rising to the surface.
# 🔹 How Bubble Sort Works

# Given:
# [5, 1, 4, 2, 8]
# Pass 1:
# Compare adjacent elements:
# 5 > 1 → swap → [1, 5, 4, 2, 8]
# 5 > 4 → swap → [1, 4, 5, 2, 8]
# 5 > 2 → swap → [1, 4, 2, 5, 8]
# 5 < 8 → no swap
# Largest element (8) settles at the end.

# Pass 2:
# 1 < 4 → no swap
# 4 > 2 → swap → [1, 2, 4, 5, 8]
# 4 < 5 → no swap
# Second largest is fixed.
# Continue until no swaps are needed.


# Bubble Sort works on:
# 1️⃣ Comparison Technique
# It compares adjacent elements.

# 2️⃣ Exchange (Swapping) Technique
# It swaps elements when they are out of order.

# 3️⃣ Internal Sorting
# Data must fit in main memory (RAM).

# ALgorithm:


nums = [10, 7, 9, 3, 4, 1, 2]

def bubble_sort(nums):
    n= len(nums)

    for i in range (n-1, 0-1, -1):
        max_ind_num = i
        for j in range (0,i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
            
print(bubble_sort(nums))



# here time complexity is O(N^2)
# here in first pass time complexity = n
# in second pass = n-1
# ....
# in last pass = 1
# so 1 + 2 + 3 + ..... + n = n(n+1)/2 = O(n^2)
#
# SC = O(1)




# in best case 
nums = [10, 7, 9, 3, 4, 1, 2]

def bubble_sort(nums):
    n= len(nums)
    
    for i in range (n-1, 0-1, -1):
        is_swap = False
        max_ind_num = i
        for j in range (0,i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            is_swap = True

        if is_swap == False:
            break

    return nums
            
print(bubble_sort(nums))

# in this case if we add is_swap flase then in best case if all are sort then loop automatically break and no further iteration
# and in best case the time complexity is O(N)
