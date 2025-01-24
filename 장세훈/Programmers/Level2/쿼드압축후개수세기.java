class 쿼드압축후개수세기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/68936
     */

    public int[] solution(int[][] arr) {
        int[] answer = new int[2];
        int n = arr.length;
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{0, 0, n, n, n});

        while (!queue.isEmpty()) {
            int[] poll = queue.pollFirst();
            boolean isOk = true;
            int base = arr[poll[0]][poll[1]];

            for (int i = poll[0]; i < poll[2]; i++) {
                for (int j = poll[1]; j < poll[3]; j++) {
                    if (arr[i][j] != base) {
                        isOk = false;
                        break;
                    }
                }

                if (!isOk) break;
            }

            if (!isOk) {
                queue.addLast(new int[]{poll[0], poll[1], poll[0] + poll[4] / 2, poll[1] + poll[4] / 2, poll[4] / 2});
                queue.addLast(new int[]{poll[0], poll[1] + poll[4] / 2, poll[0] + poll[4] / 2, poll[1] + poll[4], poll[4] / 2});
                queue.addLast(new int[]{poll[0] + poll[4] / 2, poll[1], poll[0] + poll[4], poll[1] + poll[4] / 2, poll[4] / 2});
                queue.addLast(new int[]{poll[0] + poll[4] / 2, poll[1] + poll[4] / 2, poll[0] + poll[4], poll[1] + poll[4], poll[4] / 2});
            } else
                answer[base]++;

        }

        return answer;
    }
}