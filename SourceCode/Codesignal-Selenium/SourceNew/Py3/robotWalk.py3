def robotWalk(a):
    p = q = r = s = 0
    for i in a:
        if 0 < p <= r and (q <= i or 0 <= q - s <= i and r - p <= t):
            return True
        p, q, r, s, t = i, p, q, r, s
    return False