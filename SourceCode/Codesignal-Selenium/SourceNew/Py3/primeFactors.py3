def primeFactors(n):
    r = 2
    o = []
    while n > 1:
        if n%r==0:
            o += [r]
            n //= r
        else:
            r += 1
    return o
