def lateRide(n):
    return int((n / 60) / 10) + int((n / 60) % 10) + int((n % 60) / 10) + int((n % 60) % 10)