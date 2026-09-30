def fun(x, N):
    if N==0:
        return
    print(x)
    fun(x, N-1)

fun(10,9)