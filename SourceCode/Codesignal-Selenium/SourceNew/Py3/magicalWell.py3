def magicalWell(a, b, n):
    m = 0
    while n > 0:
        m += a * b
        a += 1
        b += 1
        n -= 1
    return m