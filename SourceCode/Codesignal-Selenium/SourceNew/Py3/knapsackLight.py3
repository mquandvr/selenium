def knapsackLight(v1, w1, v2, w2, mW):
    return v1 + v2 if w1 + w2 <= mW else (v1 if v1 > v2 and w1 <= mW else (v2 if w2 <= mW else (v1 if w1 <= mW else 0)))