class 연속된부분수열의합 {

  /*
    https://school.programmers.co.kr/learn/courses/30/lessons/178870/solution_groups?language=java
   */

    public int[] solution(int[] sequence, int k) {
        int[] answer = null;
        int lt = 0, rt = 0;
        int sum = sequence[0];

        while (lt <= rt) {
            if (sum == k) {
                if (answer == null)
                    answer = new int[]{lt, rt};
                else if (rt - lt < answer[1] - answer[0])
                    answer = new int[]{lt, rt};

                if (rt + 1 < sequence.length)
                    sum += sequence[++rt];
                sum -= sequence[lt++];
            } else if (sum > k) {
                sum -= sequence[lt++];
            } else {
                if (rt + 1 < sequence.length)
                    sum += sequence[++rt];
                else break;
            }
        }

        return answer;
    }
}