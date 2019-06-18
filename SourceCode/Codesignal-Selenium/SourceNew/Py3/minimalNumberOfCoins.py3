from functools import lru_cache

def minimalNumberOfCoins(c, p):

    @lru_cache(None)
    def dp(p):
        if p == 0: return 0
        if p < 0: return float('inf')
        return 1 + min(dp(p-i) for i in c)
    return dp(p)
