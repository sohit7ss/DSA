s = "nitin"
l = len(s)-1
def func(s, l, i):
    if s[i] == s[l]:
        if i >= l:
            print("this is palindrome")
            return
        return func(s, l-1, i+1)
            
    else:
        print("not a palindrome")
        return  

func(s, l, 0)
# TC = O(n/2) = O(n)
# SC = O(n/2) = O(n)
def func1(s, l, i):
    if s[i] != s[l]:
        print("not a palindrome")
        return False
    if i >= l:
        print("this is palindrome")
        return True     
    return func(s, l-1, i+1)

func1(s,l,0)

# TC = O(n/2) = O(n)
# SC = O(n/2) = O(n)