def toggle_ith_bits(nums, i):
    new_nums = (nums ^ (1<<i))
    return new_nums

print(toggle_ith_bits(13,2))