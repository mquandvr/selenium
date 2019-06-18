def fractionSum(a, b):
    new = [a[0]*b[1] + a[1]*b[0], a[1]* b[1]]
    return [new[0]//math.gcd(new[0], new[1]), new[1]//math.gcd(new[0], new[1])]
