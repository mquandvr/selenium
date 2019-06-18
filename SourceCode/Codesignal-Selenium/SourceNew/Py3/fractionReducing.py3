from fractions import Fraction
def fractionReducing(fraction):
    f = Fraction(*fraction)
    return f.numerator, f.denominator