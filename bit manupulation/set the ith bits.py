# from .int_to_binary import Int2Bibinary , Binary2Int

def set_ith_bits_brute(num, i):
    s = str(bin(num))
    s = s[:i] + "1" + s[i+1:]
    return (s)

print(set_ith_bits_brute(10,2))


# its time complexity is O(logn) 

def set_ith_bits_optimal(nums, i):
    new_num = (nums |(1<<i))
    return new_num

# its time complexity is O(1)
# and also its space complexity is O(1)


print(set_ith_bits_optimal(10,2))