class InsertInterval {
  /*
    https://leetcode.com/problems/insert-interval/
   */
  public int[][] insert(int[][] intervals, int[] newInterval) {
    List<int[]> result = new ArrayList<>();

    boolean added = false;
    for (int[] itv : intervals) {
      if (added || itv[1] < newInterval[0]) {
        result.add(itv);
      } else if (itv[0] > newInterval[1]) {
        result.add(newInterval);
        result.add(itv);
        added = true;
      } else {
        newInterval[0] = Math.min(newInterval[0], itv[0]);
        newInterval[1] = Math.max(newInterval[1], itv[1]);
      }
    }

    if (!added) {
      result.add(newInterval);
    }

    return result.toArray(new int[result.size()][]);
  }
}