class 서버증설횟수 {

   /*
        https://school.programmers.co.kr/learn/courses/30/lessons/389479
    */

    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Deque<int[]> queue = new ArrayDeque<>();

        int server = 0;
        for (int i = 0; i < players.length; i++) {

            if (!queue.isEmpty()) {
                int[] peek = queue.peekFirst();
                if (peek[1] == i) {
                    server -= queue.poll()[0];
                }
            }

            if ((players[i] - server) / m >= 1) {
                int newServer = (players[i] - server) / m;
                server += newServer * m;
                answer += newServer;
                queue.addLast(new int[]{newServer * m, i + k});
            }

        }

        return answer;
    }
}