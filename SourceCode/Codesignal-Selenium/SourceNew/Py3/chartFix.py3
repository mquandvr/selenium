def chartFix(chart):
    toRemove = []
    for i in range(len(chart)):
        cur = i
        for j in range(i):
            if chart[j] < chart[i]:
                cur = min(cur, toRemove[j] + i - j - 1)
        toRemove.append(cur)
    res = float('inf')
    for i in range(len(toRemove)):
        res = min(res, toRemove[i] + len(chart) - i - 1)
    return res
