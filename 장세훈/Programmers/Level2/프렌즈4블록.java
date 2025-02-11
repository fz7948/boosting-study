class 프렌즈4블록 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/17679
     */

    public int solution(int m, int n, String[] board) {
        char[][] map = new char[m][n];
        int answer = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = board[i].charAt(j);
            }
        }

        int count;
        do {
            count = brokePosition(map);
            answer += count;
        } while (count != 0);

        return answer;
    }


    int brokePosition(char[][] map) {
        Deque<int[]> queue = new ArrayDeque<>();
        int count = 0;

        for (int i = 0; i < map.length - 1; i++) {
            for (int j = 0; j < map[i].length - 1; j++) {
                if (map[i][j] != '0' && map[i][j] == map[i + 1][j] && map[i][j] == map[i][j + 1] && map[i][j] == map[i + 1][j + 1]) {
                    queue.add(new int[]{i, j});
                    queue.add(new int[]{i, j + 1});
                    queue.add(new int[]{i + 1, j});
                    queue.add(new int[]{i + 1, j + 1});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            if(map[poll[0]][poll[1]] != '0') {
                map[poll[0]][poll[1]] = '0';
                count++;
            }
        }

        for (int i = 0; i < map[0].length; i++) {
            for (int j = map.length - 1; j > 0; j--) {
                if (map[j][i] == '0') {
                    int k = j;
                    while (k > -1 && map[k][i] == '0') {
                        k--;
                    }

                    if (k > -1) {
                        map[j][i] = map[k][i];
                        map[k][i] = '0';
                    }
                }

            }
        }

        return count;
    }

}