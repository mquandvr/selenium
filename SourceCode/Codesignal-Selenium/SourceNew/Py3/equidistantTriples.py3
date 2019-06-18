def equidistantTriples(coordinates):

    ans = 0
    for i in range(len(coordinates)):
        left = i - 1
        right = i + 1
        while left >= 0 or right < len(coordinates):
            distL = coordinates[i] - coordinates[left]
            distR = coordinates[right] - coordinates[i]
            if distL == distR:
                ans += 1
                left -= 1
                right += 1
            elif distL < distR:
                left -= 1
            else:
                right += 1

    return ans
