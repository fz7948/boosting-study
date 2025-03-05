class LongestIncreasingSubsequence {

    /*
        https://leetcode.com/problems/longest-increasing-subsequence/
     */

    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int result = 1;

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                    result = Math.max(result, dp[i]);
                }
            }
        }

        return result;
    }
}