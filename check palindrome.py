n = int(input("enter your number: "))
num = n 
result = 0 

while num >0:
    ld = num % 10
    result = (result*10) + ld
    num = num//10

print(result)

print(result==n)

# here TC = O(log10(N))
# SC = O(1)


# the number which is same from left as well as from right while reading