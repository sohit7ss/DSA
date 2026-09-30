num = [5, 7, 3, 2, 6, 1, 5, 9]

def reverse_num (num,left, right):
    if left == right or left > right:
        return
    else:
        num[left], num[right] = num[right], num[left]
    return reverse_num(num, left + 1, right -1)

reverse_num(num, 2, 5)
print(num)


# TC = O()