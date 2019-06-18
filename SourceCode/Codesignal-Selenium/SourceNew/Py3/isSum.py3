def isSum(value):
    s = 0
    for i in range(1, value+1):
        s += i
        if s == value:
            return True
    return False

