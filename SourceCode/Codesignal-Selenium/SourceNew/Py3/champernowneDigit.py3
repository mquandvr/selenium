def champernowneDigit(n):
    i = 1
    a = ''
    while len(a) <= n:
        a += str(i)
        i += 1
    return int(a[n-1])
        

