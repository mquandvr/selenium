def rounders(n):
    n = [int(i) for i in str(n)]
    for i in range(1,len(n)):
        if n[~i+1] >= 5: 
            n[~i] += 1
        n[~i+1] = 0
    return int("".join([str(i)for i in n]))
