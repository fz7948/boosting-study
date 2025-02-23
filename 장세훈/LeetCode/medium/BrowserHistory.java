class BrowserHistory {

  /*
      https://leetcode.com/problems/design-browser-history/
   */

  List<String> list = new ArrayList<>();
  int index = 0;

  public BrowserHistory(String homepage) {
    list.add(homepage);
  }

  public void visit(String url) {
    list = list.subList(0, index + 1);
    list.add(url);
    index = list.size() - 1;
  }

  public String back(int steps) {
    if (index < steps) {
      index = 0;
    } else {
      index -= steps;
    }

    return list.get(index);
  }

  public String forward(int steps) {
    if (index + steps >= list.size()) {
      index = list.size() - 1;
    } else {
      index += steps;
    }
    return list.get(index);
  }
}