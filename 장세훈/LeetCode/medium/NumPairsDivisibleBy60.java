class NumPairsDivisibleBy60 {
    /*
        https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
     */

    int answer = 0;

    public int numPairsDivisibleBy60(int[] time) {
        dfs(time, 0, 0, 0);
        return answer;
    }

    void dfs(int[] time, int idx, int sum, int size) {
        if (size == 2) {
            if (sum % 60 == 0)
                answer++;
            return;
        }

        for (int i = idx; i < time.length; i++) {
            dfs(time, i + 1, sum + time[i], size + 1);
        }
    }
}