class 야근지수 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12927
     */

    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        for (int work : works) {
            pq.add(work);
        }

        while (n > 0 && !pq.isEmpty()) {
            pq.add(pq.poll() - 1);
            n--;
        }

        for (Integer i : pq) {
            if (i > 0)
                answer += i * i;
        }

        return answer;
    }
}