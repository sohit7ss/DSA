n = int(input("Enter your number: "))
num = n
mod = len(str(n))
result = 0
while num>0:
    ld = num %10
    result = result + ld**mod
    num = num//10

print(result)
print(result == n)

# TC = O(log10(N))
# TC = O(1)

