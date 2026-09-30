a = [100, 30, 50, 60, -90, -40, 99, 40, 20, 25]

def largest_numer(arr):
    largest = arr[0]
    for num in arr:
        largest = max(largest, num)
        # if num > largest:
        #     largest = num

    return largest

print(largest_numer(a))