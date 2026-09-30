# Radix Sort
# Radix Sort is a non-comparison sorting algorithm that sorts numbers digit by digit, starting from either the least significant digit (LSD) or the most significant digit (MSD).
# Instead of comparing whole numbers, it groups numbers according to their digits (radix/base) and sorts them step by step.
# Technique Used
# Radix Sort works using:
# Digit-by-digit sorting
# Bucket / Counting technique
# Usually uses Counting Sort as a subroutine
# It is also a non-comparison based sorting algorithm.
# Basic Idea
# Numbers are sorted based on their digits:
# Sort by units place
# Sort by tens place
# Sort by hundreds place
# Continue until the largest digit position


# example
# Array:
# [170, 45, 75, 90, 802, 24, 2, 66]
# Step 1 – Sort by units digit
# Number	Units
# 170	0
# 45	5
# 75	5
# 90	0
# 802	2
# 24	4
# 2	2
# 66	6
# Sorted by units →
# [170, 90, 802, 2, 24, 45, 75, 66]
# Step 2 – Sort by tens digit
# Result →
# [802, 2, 24, 45, 66, 170, 75, 90]
# Step 3 – Sort by hundreds digit
# Final sorted array →
# [2, 24, 45, 66, 75, 90, 170, 802]
