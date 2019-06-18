def commonPoints(l1, r1, l2, r2):
    if r1 < r2:
        r2 = r1
    if l1 > l2:
        l2 = l1
    if r2 - l2 > 1:
        return r2 - l2 - 1
    return 0