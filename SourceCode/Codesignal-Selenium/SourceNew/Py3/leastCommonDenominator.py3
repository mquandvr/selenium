from fractions import gcd

def leastCommonDenominator(denominators):
    return reduce(lambda x,y: x * y/ gcd(x,y), denominators)
