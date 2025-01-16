class 두큐합같게만들기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/118667
     */

    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = getSum(queue1);
        long sum2 = getSum(queue2);
        Deque<Integer> q1 = new ArrayDeque<>();
        Deque<Integer> q2 = new ArrayDeque<>();

        for (int i = 0; i < queue1.length; i++) {
            q1.addLast(queue1[i]);
            q2.addLast(queue2[i]);
        }

        while (!q1.isEmpty() && !q2.isEmpty()) {
            while (sum1 > sum2 && !q1.isEmpty()) {
                sum2 += q1.peekFirst();
                sum1 -= q1.peekFirst();
                q2.addLast(q1.pollFirst());
                answer++;
            }

            while (sum2 > sum1 && !q2.isEmpty()) {
                sum1 += q2.peekFirst();
                sum2 -= q2.peekFirst();
                q1.addLast(q2.pollFirst());
                answer++;
            }

            if (answer > (queue1.length + queue2.length) * 2) return -1;
            if (sum2 == sum1) break;
        }

        if (q1.isEmpty() || q2.isEmpty()) return -1;
        return answer;
    }


    long getSum(int[] arr) {
        long sum = 0;
        for (int i : arr) {
            sum += i;
        }
        return sum;
    }
}