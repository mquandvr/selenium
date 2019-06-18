boolean isSumOfConsecutive(int n) {
  for (int start = 1; start < n; start++) {
    int number = n,
        subtrahend = start;
    while (number > 0) {
      number -= subtrahend;
      subtrahend++;
    }
    if (number == 0) {
      return true;
    }
  }
  return false;
}
