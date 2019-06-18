def onlyEvenNumbers(left, right):
    res = []
    i = left
    if left %2 != 0:
        i = left + 1
    while i <= right:
        res.append(i)
        i += 2
    return res
