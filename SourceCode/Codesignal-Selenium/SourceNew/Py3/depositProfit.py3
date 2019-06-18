def depositProfit(d, r, t):
    y=0
    while t>d:
        d+=d*(r/100)
        y+=1
    return y