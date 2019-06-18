def countWaysToChangeDigit(value):
    count = 0
    for i in str(value):
        count += ord('9') - ord(i)
    return count