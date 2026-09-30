n= int(input("enter your number: "))

num = n

while num>0:
    last_digit = n%10
    print(last_digit)
    num = num//10
