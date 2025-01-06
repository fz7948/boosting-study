class 정수삼각형 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/43105
     */
    public int solution(int[][] triangle) {
        int answer = 0;
        int[][] dp = new int[triangle.length][triangle.length];
        dp[0][0] = triangle[0][0];

        for (int i = 0; i < triangle.length - 1; i++) {
            for (int j = 0; j < triangle[i + 1].length - 1; j++) {
                dp[i + 1][j] = Math.max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j]);
                dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1]);
            }
        }

        for (int i : dp[dp.length - 1]) {
            answer = Math.max(i, answer);
        }

        return answer;
    }
}