class SmallestDivisor {
  /*
      https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
   */
  public int smallestDivisor(int[] nums, int threshold) {
    int answer = Integer.MAX_VALUE;
    int left = 0;
    int right = 1000000;

    while (left <= right) {
      int mid = (left + right) / 2;
      int sum = 0;

      if (mid == 0) {
        left = mid + 1;
        continue;
      }

      for (int num : nums) {
        sum += (num / mid) + (num % mid != 0 ? 1 : 0);
      }

      if (sum <= threshold) {
        answer = Math.min(answer, mid);
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    return answer;
  }
}