class 디펜스게임 {

   /*
        https://school.programmers.co.kr/learn/courses/30/lessons/142085
        못풀어서 해답봄.
    */

    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        for (int e : enemy) {
            pq.add(e);
            n -= e;

            if (n < 0) {
                if (k > 0) {
                    n += pq.poll();
                    k--;
                } else break;
            }

            answer++;
        }

        return answer;
    }
}