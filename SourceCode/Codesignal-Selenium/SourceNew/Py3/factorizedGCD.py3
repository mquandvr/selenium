int factorizedGCD(int[] a, int[] b) {
  int j = 0,
      result = 1;
  for (int i = 0; i < a.length; i++) {
    while (j < b.length && a[i] > b[j]) {
      j++;
    }
    if (j < b.length && a[i] == b[j]) {
      result *= a[i];
      j++;
    }
  }
  return result;
}
