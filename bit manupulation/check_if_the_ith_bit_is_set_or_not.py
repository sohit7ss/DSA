def check_set_right_shift(nums, i):
    s = False
    if (nums & (1<<i)) != 0:
        s = True
    return s
    

print(check_set_right_shift(13, 2))

def check_set_left_shift(nums, i):
    s = False
    if ((nums >>i) & 1) == 1:
        s = True
    return s

print(check_set_left_shift(13, 1))