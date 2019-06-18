def isCaseInsensitivePalindrome(s):
    s = s.lower()
    return s == s[::-1]

