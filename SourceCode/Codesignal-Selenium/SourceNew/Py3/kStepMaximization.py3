def kStepMaximization(n, k):
    to = [0, 1, 2, -1, -1, 5, 9, -1, 8, 6]
    
    def rotate(n):
        s = [to[int(c)] for c in str(n)[::-1]]
        if any(c == -1 for c in s):
            return 0
        else:
            return int(''.join(map(str, s)))
    
    if k == 0:
        return n
    return max(kStepMaximization(n + 1, k - 1), kStepMaximization(n * 2, k - 1), kStepMaximization(rotate(n), k - 1))
