class 숫자변환하기 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/154538
     */

    public int solution(int x, int y, int n) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{x, 0});
        int answer = Integer.MAX_VALUE;
        Set<Integer> set = new HashSet<>();

        while (!queue.isEmpty()) {
            int[] poll = queue.pollFirst();
            int num = poll[0];
            int count = poll[1];

            if (set.contains(num)) continue;
            set.add(num);

            if (num == y) {
                answer = Math.min(answer, count);
            }

            if (num * 2 <= y) queue.addLast(new int[]{num * 2, count + 1});
            if (num * 3 <= y) queue.addLast(new int[]{num * 3, count + 1});
            if (num + n <= y) queue.addLast(new int[]{num + n, count + 1});
        }

        return answer == Integer.MAX_VALUE ? -1 : answer;
    }

}