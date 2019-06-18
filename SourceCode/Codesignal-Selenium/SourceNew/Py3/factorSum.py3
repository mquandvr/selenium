def factorSum(n):
    p = n
    d = 2
    nx = 0
    while d * d <= p:
        while p % d == 0:
            nx += d
            p //= d
        d += 1
    if p != 1:
        nx += p
    
    if nx == n:
        return n
    return factorSum(nx)
    
