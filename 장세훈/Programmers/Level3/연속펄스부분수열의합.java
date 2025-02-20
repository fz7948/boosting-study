class 연속펄스부분수열의합{
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/161988
     */
    public long solution(int[] sequence) {
        long answer = 0;
        int[] purseArr1 = sequence.clone();
        int[] purseArr2 = sequence.clone();

        for (int i = 0; i < sequence.length; i++) {
            if (i % 2 == 0) {
                purseArr1[i] *= -1;
            } else
                purseArr2[i] *= -1;
        }

        long[] dp1 = new long[sequence.length];
        long[] dp2 = new long[sequence.length];
        dp1[0] = purseArr1[0];
        dp2[0] = purseArr2[0];
        answer = Math.max(dp1[0], dp2[0]);

        for (int i = 1; i < sequence.length; i++) {
            dp1[i] = Math.max(dp1[i - 1] + purseArr1[i], purseArr1[i]);
            dp2[i] = Math.max(dp2[i - 1] + purseArr2[i], purseArr2[i]);
            answer = Math.max(answer, Math.max(dp1[i], dp2[i]));
        }

        return answer;
    }
}