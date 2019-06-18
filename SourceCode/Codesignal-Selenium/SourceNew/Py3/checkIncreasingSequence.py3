bool checkIncreasingSequence(std::vector<int> seq) {

  for (int i = 0; i < (int)seq.size(); i++) {
    if (seq[i] <= seq[i - 1]) {
      return false;
    }
  }

  return true;
}
