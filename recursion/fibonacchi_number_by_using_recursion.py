def func(num):
    if num == 0 or num == 1:
        return num
    return func(num-1) + func (num - 2)

print(func(9))

# TC = O(2^n)
# SC = O(2^n)
