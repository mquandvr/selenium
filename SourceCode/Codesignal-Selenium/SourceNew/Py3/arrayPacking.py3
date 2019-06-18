def arrayPacking(a):

    res = 0
    for i in range(len(a)):
        res |= (a[i] << (8 * i))

    return res
