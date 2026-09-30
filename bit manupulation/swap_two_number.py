a = 30
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

def swap_two_number(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return print(a,b)

swap_two_number(a,b)