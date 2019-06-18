int electionsWinners(int[] votes, int k) {

  int currentMaxIndex = 0;
  int cntLeaders = 0;
  int result = 0;
  for (int i = 1; i < votes.length; i++) {
    if (votes[i] == votes[currentMaxIndex]) {
      cntLeaders++;
    }
    if (votes[i] > votes[currentMaxIndex]) {
      currentMaxIndex = i;
      cntLeaders = 1;
    }
  }

  for (int i = 0; i < votes.length; i++) {
    if (votes[i] + k > votes[currentMaxIndex]) {
      result++;
    }
    if (votes[i] + k == votes[currentMaxIndex]
     && currentMaxIndex == i) {
      result++;
    }
  }

  return result;
}
