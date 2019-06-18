function isIPv4Address(inputString) {

  var currentNumber = 0;
  var emptyField = true;
  var countNumbers = 0;

  inputString += '.';

  for (var i = 0; i < inputString.length; i++) {
    if (inputString[i] === '.') {
      if (emptyField) {
        return false;
      }
      countNumbers++;
                currentNumber = 0;
                emptyField = true;
    }
    else {
      var digit = inputString.charCodeAt(i) - '0'.charCodeAt(0);
      if (digit < 0 || digit > 9) {
        return false;
      }
      emptyField = false;
      currentNumber = currentNumber * 10 + digit;
      if (currentNumber > 255) {
        return false;
      }
    }
  }
  return countNumbers === 4;
}
