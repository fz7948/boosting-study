class JumpGame2 {

    /*
        https://leetcode.com/problems/jump-game-ii/
     */
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {

            for (int j = i + 1; j <= nums[i] + i; j++) {
                if (j < nums.length) {
                    if (dp[j] != 0)
                        dp[j] = Math.min(dp[i] + 1, dp[j]);
                    else dp[j] = dp[i] + 1;
                }
            }
        }

        return dp[nums.length - 1];
    }
}