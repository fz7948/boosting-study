class 마법의엘리베이터 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/148653
     */

    public int solution(int storey) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{storey, 0});
        int answer = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();

            if (poll[0] == 0) {
                answer = Math.min(poll[1], answer);
                continue;
            }

            queue.add(new int[]{poll[0] / 10, poll[1] + poll[0] % 10});
            queue.add(new int[]{(poll[0] / 10) == 0 ? poll[0] > 5 ? 1 : 0 : (poll[0] / 10) + 1, poll[1] + 10 - (poll[0] % 10)});

        }

        return answer;
    }
}