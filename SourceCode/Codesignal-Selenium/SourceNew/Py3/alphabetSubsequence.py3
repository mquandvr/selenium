def alphabetSubsequence(s):
  for i in range(1, len(s)):
    if list(s)[i]<=list(s)[i-1]:
      return False
  return True