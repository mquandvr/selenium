int smallestNumber(int n) {

  if (n == 1) {
    return 0;
  }

  int res = 1;

  for (int i = 1; i < n; i++) {
    res *= 10;
  }

  return res;
}
