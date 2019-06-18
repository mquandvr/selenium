int digitSumsDifference(int n) {

  int result = 0;
  while (n != 0) {
    int digit = n % 10;
    if (digit % 2 == 1) {
      result -= digit % 10;
    }
    else {
      result += digit;
    }
    n /= 10;
  }

  return result;
}
