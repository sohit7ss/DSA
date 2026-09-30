# 5     20      3
# 7     -10     9
# 1     -52     6

nums = [[5,20,3], [7,-10, 9], [1,-52,6]]
nums1 = [[5,20,3], [7,-10, 9]]

# iterate the each elements of matrix

def iterate_element(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            print(nums[i][j], end="  ")
        print()

iterate_element(nums)

print()
print()


def upper_triangle(nums):
    i = 0
    for i in range(len(nums)):
        print(i*("* "), end="")
        for j in range(i, len(nums[0])):
            print(nums[i][j], end=" ")
        print()

upper_triangle(nums)

print()
print()


def upper_triangle_alter(nums):
    i = 0
    for i in range(len(nums)):
        for j in range(0, len(nums[0])):
            if j>= i:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

upper_triangle_alter(nums)

print()
print()

def lower_triangle(nums):
    # i = len(nums) -1
    for i in range(len(nums)):
        # for j in range(0,i+1):
        for j in range(0,len(nums[0])):
        #     print(nums[i][j], end=" ")
        # print(i*("* "), end="")
            if j <= i:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

lower_triangle(nums)

print()
print()

def diagonal(nums):
    if len(nums) == len(nums[0]):
        for i in range(0, len(nums)):
            print(nums[i][i])

diagonal(nums)

print()
print()


def cross_diagonal(nums):
    i = 0
    j = len(nums) -1 
    while i < len(nums):
        print(nums[i][j])
        i += 1
        j -= 1

cross_diagonal(nums)

print()
print()


def transpose(nums):
    for i in range(len(nums[0])):
        for j in range(len(nums)):
            print(nums[j][i], end="  ")
        print()

transpose(nums1)
print()
print()
transpose(nums)

def transpose_list(nums):
    rows = len(nums)
    cols = len(nums[0])

    # result = [[[0] * rows] for _ in range(cols)]
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]

    print(result)

transpose_list(nums1)