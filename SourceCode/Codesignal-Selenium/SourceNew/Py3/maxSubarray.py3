def maxSubarray(a):
    r = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            r = max(r,sum(a[i:j+1]))
    return r
            
