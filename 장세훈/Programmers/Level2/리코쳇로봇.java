class 리코쳇로봇 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/169199
        혼자 풀긴했는데 코드가 너무 지저분해서 gpt에게 리팩터링 요청함..
     */

    private static final int[] dx = {-1, 1, 0, 0}; // 상, 하, 좌, 우
    private static final int[] dy = {0, 0, -1, 1};

    private char[][] map;
    private boolean[][] visit;
    private int[] destination;

    public int solution(String[] board) {
        int n = board.length, m = board[0].length();
        map = new char[n][m];
        visit = new boolean[n][m];
        Deque<int[]> queue = new ArrayDeque<>();

        // 맵 초기화 및 시작 위치 탐색
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                map[i][j] = board[i].charAt(j);
                if (map[i][j] == 'R') {
                    queue.add(new int[]{i, j, 0});
                    visit[i][j] = true;
                } else if (map[i][j] == 'G') {
                    destination = new int[]{i, j};
                }
            }
        }

        return bfs(queue);
    }

    private int bfs(Deque<int[]> queue) {
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0], y = current[1], count = current[2];

            if (x == destination[0] && y == destination[1]) {
                return count; // 최단 거리 도달
            }

            // 네 방향으로 이동
            for (int d = 0; d < 4; d++) {
                int[] next = move(x, y, dx[d], dy[d]);
                int nx = next[0], ny = next[1];

                if (!visit[nx][ny]) {
                    queue.add(new int[]{nx, ny, count + 1});
                    visit[nx][ny] = true;
                }
            }
        }
        return -1; // 도달 불가능
    }

    private int[] move(int x, int y, int dx, int dy) {
        while (isValid(x + dx, y + dy)) {
            x += dx;
            y += dy;
        }
        return new int[]{x, y};
    }

    private boolean isValid(int x, int y) {
        return x >= 0 && y >= 0 && x < map.length && y < map[0].length && map[x][y] != 'D';
    }
}