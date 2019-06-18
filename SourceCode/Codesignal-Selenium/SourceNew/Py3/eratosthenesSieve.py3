def eratosthenesSieve(n):

    primes = []
    mayBePrime = []
    for i in range(n + 1):
        mayBePrime.append(True)
    for i in range(2, n + 1):
        if mayBePrime[i]:
            primes.append(i)
            j = i
            while i * j <= n:
                mayBePrime[i * j] = False
                j += 1

    return primes
