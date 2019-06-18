def primeFactors2(n):
    out = []
    for i in range(2, n+1):
        if n % i == 0:
            out.append(i)
        while n % i ==0:
            n = n // i
    return out
