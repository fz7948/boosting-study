class 지게차와크레인 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/388353
     */

    public int solution(String[] storage, String[] requests) {
        int answer = storage.length * storage[0].length();
        char[][] map = new char[storage.length][storage[0].length()];
        Deque<int[]> queue = new ArrayDeque<>();

        for (int i = 0; i < storage.length; i++) {
            for (int j = 0; j < storage[0].length(); j++) {
                map[i][j] = storage[i].charAt(j);
            }
        }

        for (String request : requests) {
            for (int i = 0; i < storage.length; i++) {
                for (int j = 0; j < storage[0].length(); j++) {
                    if (request.charAt(0) == map[i][j]) {
                        if (request.length() == 2 || bfs(map, i, j)) {
                            queue.add(new int[]{i, j});
                        }
                    }
                }
            }

            answer -= queue.size();
            while (!queue.isEmpty()) {
                int[] poll = queue.poll();
                map[poll[0]][poll[1]] = ' ';
            }
        }

        return answer;
    }

    boolean bfs(char[][] map, int px, int py) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{px, py});
        int[][] direct = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        boolean[][] visit = new boolean[map.length][map[0].length];
        visit[px][py] = true;

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            int x = poll[0];
            int y = poll[1];

            if (x == 0 || y == 0 || x == map.length - 1 || y == map[0].length - 1) {
                return true;
            }

            for (int[] d : direct) {
                int nx = x + d[0];
                int ny = y + d[1];

                if (nx > -1 && ny > -1 && nx < map.length && ny < map[0].length && !visit[nx][ny] && map[nx][ny] == ' ') {
                    queue.add(new int[]{nx, ny});
                    visit[nx][ny] = true;
                }
            }
        }

        return false;
    }
}