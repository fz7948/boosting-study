class SimplifyPath {

  /*
      https://leetcode.com/problems/simplify-path/
   */
  public String simplifyPath(String path) {
    String[] split = path.split("/");
    Deque<String> queue = new ArrayDeque<>();

    for (String s : split) {
      if (s.isEmpty() || s.equals(".")) {
        continue;
      } else if (s.equals("..")) {
        if (!queue.isEmpty()) {
          queue.pollLast();
        }
      } else {
        queue.addLast(s);
      }
    }

    StringBuilder sb = new StringBuilder();
    while (!queue.isEmpty()) {
      sb.append("/").append(queue.pollFirst());
    }

    return sb.isEmpty() ? "/" : sb.toString();
  }

}