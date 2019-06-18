def kthDivisor(n, k):
    n = [i for i in range(1,n+1) if n%i==0]
    return -1 if len(n) < k else n[k-1]
