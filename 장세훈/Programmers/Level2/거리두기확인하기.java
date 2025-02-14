class 거리두기확인하기 {

     /*
        https://school.programmers.co.kr/learn/courses/30/lessons/81302
     */

    public int[] solution(String[][] places) {
        List<Integer> answer = new ArrayList<>();
        for (String[] place : places) {
            char[][] map = new char[5][5];
            for (int i = 0; i < place.length; i++) {
                for (int j = 0; j < place[0].length(); j++) {
                    map[i][j] = place[i].charAt(j);
                }
            }
            if (isOk(map)) answer.add(1);
            else answer.add(0);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    boolean isOk(char[][] map) {
        int[][] direct = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (map[i][j] == 'P') {
                    Deque<int[]> queue = new ArrayDeque<>();
                    boolean[][] visit = new boolean[5][5];

                    queue.add(new int[]{i, j, 0});
                    visit[i][j] = true;

                    while (!queue.isEmpty()) {
                        int[] poll = queue.poll();
                        int x = poll[0];
                        int y = poll[1];
                        int dist = poll[2];

                        if (dist > 2) continue;
                        if (dist >= 1 && map[x][y] == 'P') return false;

                        for (int[] d : direct) {
                            int nx = x + d[0];
                            int ny = y + d[1];

                            if (nx > -1 && nx < 5 && ny > -1 && ny < 5 && !visit[nx][ny] && map[nx][ny] != 'X') {
                                queue.add(new int[]{nx, ny, dist + 1});
                                visit[nx][ny] = true;
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
}