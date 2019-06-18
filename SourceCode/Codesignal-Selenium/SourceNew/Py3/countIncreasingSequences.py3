def countIncreasingSequences(n, k):
    u=1
    for i in range(n):
        u=((k-i)*u)/(i+1)
    return u
