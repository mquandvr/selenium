def nearestRoundNumber(v):
    return (v//10+1)*10 if v%100!=0 else v

