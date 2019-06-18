def checkSameElementExistence(arr1, arr2):
  return len({*arr1}) + len({*arr2}) > len({*(arr1+arr2)})
