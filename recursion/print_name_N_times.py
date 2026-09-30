def n_times(N):
    if N == 0:
        return
    n_times(N-1)
    print("hello")

n_times(10)