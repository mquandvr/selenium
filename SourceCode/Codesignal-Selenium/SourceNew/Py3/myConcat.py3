String myConcat(String[] strings, String separator) {

  String result = "";
  for (int i = 0; i < strings.length; i++) {
    result+= strings[i] + separator;
  }
  return result;
}
