def counting(i, n):
    if i >n:
        return                          #-------> this is used for normal order and this is a head recursion. in this recursion first job will done then function call  
    print(i)
    counting(i+1, n)

def counting1(i, n):
    if i >n:
        return                          #-------> this is used for reverse order and this is a tail recursion. in this recursion forst function will call then job will be done from end of the all funtion in reverser order
    counting1(i+1, n)
    print(i)
    
def c_rev_head(n,i):
    if i >n:
        return
    print(n)
    c_rev_head(n-1,i)

counting(4,20)
counting1(4,20)
c_rev_head(25, 20)
