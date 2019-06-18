String getMonthName(int mo) {
  mo--;
  String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
      "Aug", "Sep", "Oct", "Nov", "Dec"};
  if (mo >= 0 && mo < months.length) {
    return months[mo];
  } else {
    return "invalid month";
  }
}
