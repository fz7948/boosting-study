class 아이템줍기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/87694?language=java
        좌표를 2배로 늘림으로 직선의 방향 정보를 저장할 수 있음.
     */
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        Set<Path> possible = new HashSet<>();
        Set<Path> imPossible = new HashSet<>();
        boolean[][] visit = new boolean[102][102];

        for (int[] rec : rectangle) {
            int x1 = rec[0] * 2, y1 = rec[1] * 2;
            int x2 = rec[2] * 2, y2 = rec[3] * 2;

            for (int i = x1; i <= x2; i++) {
                for (int j = y1; j <= y2; j++) {
                    Path path = new Path(i, j);
                    if (i == x1 || i == x2 || j == y1 || j == y2) {
                        if (!imPossible.contains(path))
                            possible.add(path);
                    } else {
                        imPossible.add(path);
                        possible.remove(path);
                    }
                }
            }
        }

        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{characterX * 2, characterY * 2, 0});
        int[][] direct = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!queue.isEmpty()) {
            int[] poll = queue.pollFirst();
            int nowX = poll[0];
            int nowY = poll[1];
            int count = poll[2];

            if (nowX == itemX * 2 && nowY == itemY * 2) {
                answer = count / 2;
                break;
            }

            for (int[] d : direct) {
                int newX = nowX + d[0];
                int newY = nowY + d[1];
                if (possible.contains(new Path(newX, newY)) && !visit[newX][newY]) {
                    queue.addLast(new int[]{newX, newY, count + 1});
                    visit[newX][newY] = true;
                }
            }
        }

        return answer;
    }

    class Path {
        int x;
        int y;

        public Path(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (o == null || getClass() != o.getClass()) return false;
            Path path = (Path) o;
            return x == path.x && y == path.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

}