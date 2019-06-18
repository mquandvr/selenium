def maximalAllowableSubarrays(inputArray, maxSum):
    ans = [0] * len(inputArray)
    
    sm = 0
    i, j = 0, -1
    while i < len(inputArray):
        while j < len(inputArray) - 1 and sm + inputArray[j + 1] <= maxSum:
            sm += inputArray[j + 1]
            j += 1
        print(sm)
        ans[i] = j
        sm -= inputArray[i]
        i += 1
        j = max(j, i - 1)
    return ans
