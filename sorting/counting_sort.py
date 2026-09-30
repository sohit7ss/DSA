# Counting Sort is a non-comparison-based sorting algorithm that sorts elements by counting how many times each distinct value appears.
# It works efficiently when:
# The input elements are integers
# The range of values (k) is not very large
# 🔹 Technique Used
# Counting Sort works on:
# Counting / Frequency technique
# Non-comparison sorting
# Direct indexing method
# Unlike Quick or Merge Sort, it does not compare elements.
# 🔹 Basic Idea
# If you know:
# How many times each number appears
# And how many numbers are smaller than it
# Then you can directly place each element at its correct position.
# 🔹 Example
# Unsorted array:
# [4, 2, 2, 8, 3, 3, 1]
# Step 1: Find Maximum Value
# Max = 8
# Create count array of size 9 (0–8)
# Step 2: Count Frequency
# Count array:
# Index: 0 1 2 3 4 5 6 7 8
# Count: 0 1 2 2 1 0 0 0 1
# Step 3: Cumulative Count
# 0 1 3 5 6 6 6 6 7
# This tells us the final position of elements.
# Step 4: Build Sorted Output
# Final sorted array:
# [1, 2, 2, 3, 3, 4, 8]
# 🔹 Algorithm
# Find maximum value (k)
# Create count array of size k+1
# Count occurrences
# Convert count array to cumulative count
# Place elements in output array

# python implementation

arr = [4, 2, 2, 8, 3, 3, 1]

# here we have fixed range like in this list the numbers are in between 1-9
# so we create 9 index with value 0

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = []

    for num in arr:
        count[num] +=1

    for i in range(len(count)):
        for j in range(count[i]):                   # remember this code
            sorted_arr.append(i)



    return sorted_arr
print(counting_sort(arr))

