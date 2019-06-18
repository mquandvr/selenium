def isOneSwapEnough(inputString):
    n=len(inputString)
    if n==1:
        return True
    a=list(inputString)
    for i in range (n):
        for j in range (n):
            a[i],a[j]=a[j],a[i]
            if a==a[::-1]:
                return True
            a[i],a[j]=a[j],a[i]
    return False
