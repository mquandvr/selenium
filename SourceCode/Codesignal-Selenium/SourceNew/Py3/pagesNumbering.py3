def pagesNumbering(n):
    r = 0
    k = 9
    while n>0:
        r+=n
        n-=k
        k*=10
    return r
