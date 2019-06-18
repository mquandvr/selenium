int stringsCrossover(String[] inputArray,
                     String result) {

  int answer = 0;

  for (int i = 0; i < inputArray.length; i++) {
    for (int j = i + 1; j < inputArray.length; j++) {
      boolean correct = true;
      for (int k = 0; k < result.length(); k++) {
        if (result.charAt(k) != inputArray[i].charAt(k)
            && result.charAt(k) != inputArray[j].charAt(k)) {
          correct = false;
          break;
        }
      }
      if (correct) {
        answer++;
      }
    }
  }
  return answer;
}
