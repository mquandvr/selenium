from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    map(lambda x: res[x].rotate(-x), range(n))
    return [list(d) for d in res]
