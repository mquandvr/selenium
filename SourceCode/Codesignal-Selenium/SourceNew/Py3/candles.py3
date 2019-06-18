def candles(candlesNumber, makeNew):
    ct = 0
    waste = 0
    while candlesNumber > 0:
        ct += 1
        waste += 1
        candlesNumber -= 1
        if waste >= makeNew:
            waste -= makeNew
            candlesNumber += 1
    return ct
