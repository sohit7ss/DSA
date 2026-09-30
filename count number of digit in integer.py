# method 1

n = int(input("enter your number: "))
num = n
count = 0
while num>0:
    count = count + 1
    num = num//10

print(count)

# here time complexity , TC = O(log10(N))
# SC = O(1)

# method 2

from math import *

def count_digit(num):
    print(int(log10(num)+1))
    return int(log10(num)+1)

num = 12345
count_digit(num)

# TC = O(1)
# SC = O(1)
