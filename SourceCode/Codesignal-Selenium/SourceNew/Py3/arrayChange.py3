def arrayChange(a):
    r = 0
    for i in range(1,len(a)):
        if a[i] <= a[i-1]:
            r += a[i-1]-a[i]+1
            a[i] = a[i] + a[i-1]-a[i]+1
            print(r)
    return r
