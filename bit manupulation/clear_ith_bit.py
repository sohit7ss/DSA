def clear_ith_bit_optimal(num, i):
    new_num = (num & ~(1 << i))
    return new_num

print(clear_ith_bit_optimal(10,1))