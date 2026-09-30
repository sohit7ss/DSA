num = [5, 7, 3, 2, 6, 1, 5, 9]

left = 2
right = 5

while left < right:
    num[left], num[right] = num[right], num[left]
    left += 1
    right -= 1

print(num)