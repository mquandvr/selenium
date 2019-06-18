def countSumOfTwoRepresentations2(n, l, r):
    c = 0
    for a in range(l, r+1):
        b = n - a
        if l <= a <= b <= r:
            c += 1
    return c

