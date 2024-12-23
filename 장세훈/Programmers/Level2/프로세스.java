class 프로세스 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=java
     */

    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        Deque<Integer> queue = new ArrayDeque<>();
        int answer = 0;

        for (int priority : priorities) {
            pq.add(priority);
            queue.addLast(priority);
        }

        while (!queue.isEmpty()) {
            Integer poll = queue.pollFirst();

            if (Objects.equals(pq.peek(), poll)) {
                answer++;
                pq.poll();

                if (location == 0) break;

            }

            queue.addLast(poll);
            location--;
            if (location == -1) location = queue.size() - 1;
        }

        return answer;
    }
}