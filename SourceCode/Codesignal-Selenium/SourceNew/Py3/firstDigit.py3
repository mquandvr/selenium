char firstDigit(std::string inputString) {
  std::regex regex("[0-9]");
  std::smatch match;
  if (regex_search(inputString, match, regex)) {
    std::ssub_match sub_match = match[0];
    return sub_match.str()[0];
  }
}
