# m-1

n = int(input("Enter your number: "))

num = n
facor = []
for i in range (1,n+1):
    if num % i == 0:
        facor.append(i)
print(facor)

# this is brute force method in which we check all number 
# which means time complexity incerease

# TC = O(N)
# SC = O(K)


# M - 2

facor_1 = []
for j in range (1, n//2+ 1):
    if num % j == 0:
        facor_1.append(j)

facor_1.append(num)
print(facor_1)

# this is better method but not optimal method 
#  TC = O(N/2) = O(N)
#  SC = O(K)


# M - 3

from math import sqrt
factor = []

for i in range (1, int(sqrt(num) + 1)):
    if num % i == 0:
        factor.append(i)
        if num // i != n:
            factor.append(num//i)
factor.append(n)
print(factor)

factor.sort()
print(factor)

# this is optimal and best way 
#  TC = O(root(N)) + O(Nlog(N))
# SC = O(K)