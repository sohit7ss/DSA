def fact_of_num(n):
    if n == 1 or n==0:
        return 1
    return n * fact_of_num(n-1)

print(fact_of_num(5))

# TC = O(N)
# SC = O(N) due to stack space