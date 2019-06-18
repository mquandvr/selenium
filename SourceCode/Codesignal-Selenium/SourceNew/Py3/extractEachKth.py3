def extractEachKth(a, k):
    return [x for i, x in enumerate(a) if (i+1)%k!=0]
    
