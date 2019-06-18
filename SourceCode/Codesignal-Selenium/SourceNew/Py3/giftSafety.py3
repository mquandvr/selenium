def giftSafety(gift):
    c = 0
    for i in range(len(gift)-2):
        if len(set(list(gift[i:i+3]))) < 3:
            c += 1
    return c