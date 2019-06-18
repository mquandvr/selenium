def firstMultiple(divisors, s):
  while 1:
    if all(s%d==0 for d in divisors):
      return s
    s += 1
