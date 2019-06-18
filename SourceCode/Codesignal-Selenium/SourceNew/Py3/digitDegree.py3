def digitDegree(n):
    c=0
    while n>9:
        ans=0
        for i in str(n):
            ans+=int(i)
        n=ans
        c+=1
    return c