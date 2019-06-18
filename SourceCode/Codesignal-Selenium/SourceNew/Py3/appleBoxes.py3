def appleBoxes(k):

    sum = 0
    x = 0
    while x <= k:
        if x % 2 == 1:
            sum += x * x
        else:
            sum -= x * x
        x += 1

    return -sum
