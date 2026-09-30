arr = [3, 4, 5, 2, 8, 10, 6, 1]
def right_rotate_by_1_with_slicing (arr):
    n = len(arr)
    arr[:] = arr[-1:] + arr[0: n-1]
    return arr

print(right_rotate_by_1_with_slicing(arr))

# TC = O(1) + O(n-1) == O(n)
# SC = O(1)

def right_rotate_by_without_slicing(arr):
    n= len(arr)
    temp = arr[n-1]
    for i in range (n-2, -1 , -1):
        arr[i+1] = arr[i]

    arr[0] = temp
    return arr

print(right_rotate_by_without_slicing(arr))

# TC = O(n-1) == O(n)
# SC = O(1)