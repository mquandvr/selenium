def toAndFro(a, b, t):
    l = abs(b - a)
    t %= 2 * l
    if t <= l:
        return a + (b - a) / abs(b - a) * t
    else:
        t -= l
        return b + (a - b) / abs(a - b) * t
