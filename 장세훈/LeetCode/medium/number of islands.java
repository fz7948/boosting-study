class NumberOfIslands {
    /*
        200. Number of Islands
        https://leetcode.com/problems/number-of-islands/description/

        섬의 개수 세는 문제
        stack을 활용하 bfs로 문제를 풀이함.
          2차원 배열을 순회하면서 1이 나오면
            answer++
            1의 위치를 기준으로 상하좌우 위치를 스택에 넣고 뺴며 섬을 지워나감

     */

    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        int answer = 0;
        int[][] dir = new int[][]{{1, 0}, {0, -1}, {-1, 0}, {0, 1}};


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    answer++;
                    Deque<int[]> stack = new ArrayDeque<>();
                    stack.push(new int[]{i, j});

                    while (!stack.isEmpty()) {
                        int[] pop = stack.pop();
                        grid[pop[0]][pop[1]] = '0';

                        for (int k = 0; k < 4; k++) {
                            int nx = dir[k][0] + pop[0];
                            int ny = dir[k][1] + pop[1];

                            if (nx > -1 && nx < n && ny > -1 && ny < m && grid[nx][ny] == '1') {
                                grid[nx][ny] = '0';
                                stack.add(new int[]{nx, ny});
                            }
                        }
                    }
                }
            }
        }

        return answer;
    }
}