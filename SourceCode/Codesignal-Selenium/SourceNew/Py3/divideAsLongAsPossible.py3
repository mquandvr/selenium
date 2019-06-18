def divideAsLongAsPossible(n, d):

    while n % d == 0:
        n=n/d
    return n
