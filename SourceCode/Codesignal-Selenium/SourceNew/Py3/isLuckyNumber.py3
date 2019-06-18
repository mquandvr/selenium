def isLuckyNumber(n):
    return all([i=="7" or i=="4" for i in str(n)])