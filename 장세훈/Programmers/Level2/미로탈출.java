class 미로탈출 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/159993?language=java
        (시작점 -> 레버) 거리 + ( 레버 + 도착점) 거리
     */

    public int solution(String[] maps) {
        int[] start = null;
        int[] lever = null;
        int[] exit = null;

        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length(); j++) {
                if (maps[i].charAt(j) == 'S') {
                    start = new int[]{i, j};
                } else if (maps[i].charAt(j) == 'L') {
                    lever = new int[]{i, j};
                } else if (maps[i].charAt(j) == 'E') {
                    exit = new int[]{i, j};
                }
            }
        }

        int toLever = getDistance(start, lever, maps);
        int toExit = getDistance(lever, exit, maps);

        if (toLever == -1 || toExit == -1) return -1;
        else return toLever + toExit;
    }

    int getDistance(int[] from, int[] to, String[] maps) {
        boolean[][] visit = new boolean[maps.length][maps[0].length()];
        int[][] d = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{from[0], from[1], 0});

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            int x = poll[0];
            int y = poll[1];
            int t = poll[2];

            if (to[0] == x && to[1] == y) {
                return t;
            }

            for (int i = 0; i < d.length; i++) {
                int nx = x + d[i][0];
                int ny = y + d[i][1];
                if (nx > -1 && nx < maps.length && ny > -1 && ny < maps[0].length() && !visit[nx][ny] && maps[nx].charAt(ny) != 'X') {
                    visit[nx][ny] = true;
                    queue.add(new int[]{nx, ny, t + 1});
                }
            }
        }

        return -1;
    }
}