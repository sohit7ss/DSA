def Int2Bibinary(num:int) -> str:
    result = " "
    while num > 0 :
        if num %2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        num = num//2
    return result

# Strings are immutable
# So every time:
# A new string is created
# Old string is copied
# If current length = k, then:
# concatenation cost = O(k)
# ⚙️ Step 3: Total cost calculation
# Let number of iterations = log n
# String lengths grow like:
# 1 + 2 + 3 + ... + log n
# Total work:
# O(1 + 2 + 3 + ... + log n)
# = O((log n)²)
# ✅ Final Answer
# ⏱️ Time Complexity:
# O((log n)²)
# ⚠️ Most students get this wrong
# They say:
# O(log n)
# That’s only for the loop — ignores string cost

# here space complexity is  O(log2(n))

def Binary2Int(x:str) -> int:
    decimal_num = 0
    power = len(x) -1
    for ch in x:
        decimal_num = decimal_num + (2**power)*int(ch)
        power -= 1
    return decimal_num
# its time complexity is O(len)


print(Int2Bibinary(15))
print(Binary2Int("1111"))