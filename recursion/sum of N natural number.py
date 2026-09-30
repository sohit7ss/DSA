# sum of n natural numnber

def sum_of_n_natural_number (n):
    if n==1:
        return 1
    return n + sum_of_n_natural_number(n-1)
    
    

print(sum_of_n_natural_number(5))

# here time complexity is O(N) cuz here here code calls n times 
# and space complexity is O(N) due to N stacks are created 
# stack is a In Python, stack space refers to the memory used to manage function calls during execution.

# Python maintains a call stack internally.
# Each function call creates a stack frame that stores:

# Local variables

# Function arguments

# Return address

# Execution state

# When the function finishes, its frame is automatically removed.
