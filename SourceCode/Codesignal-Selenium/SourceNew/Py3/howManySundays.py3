def howManySundays(n, startDay):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    i = days.index(startDay)
    a = 0
    for j in range(n):
        i = (i+1) % 7
        if i == 0:
            a += 1
        
    return a