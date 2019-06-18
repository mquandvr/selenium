def divNumber(k, l, r):
    c = 0
    for i in range(l, r+1):
        if i != 0 and countDiv(i) == k:
            c+= 1
    return c
def countDiv(n):
    r = 0
    for i in range(n+1):
        if i != 0 and n%i == 0 :
            r+=1
    return r