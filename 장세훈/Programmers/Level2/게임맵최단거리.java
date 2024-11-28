class 게임맵최단거리 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/1844

        bfs 문제
        
        큐에 좌표를 넣는 시점에 방문 처리를 해야 한다.
        그렇지 않으면 시간초과 발생.
    */
    public static void main(String[] args) {
        System.out.println(new 게임맵최단거리().solution(
                new int[][]{
                        {1, 1, 1},
                        {1, 1, 1},
                        {1, 1, 1},
                        {1, 1, 0},
                        {1, 1, 0}
                }
        ));
    }

    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.get(2)));
        pq.add(List.of(0, 0, 1));
        int[][] direct = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        maps[0][0] = 0;

        while (!stack.isEmpty()) {
            List<Integer> pos = stack.poll();
            Integer x = pos.get(0);
            Integer y = pos.get(1);
            Integer c = pos.get(2);


            if (x == n - 1 && y == m - 1)
                return c;

            for (int[] d : direct) {
                int nx = d[0] + x;
                int ny = d[1] + y;
                if (nx > -1 && nx < n && ny > -1 && ny < m && maps[nx][ny] == 1) {
                    pq.add(List.of(nx, ny, c + 1));
                    maps[nx][ny] = 0;
                }
            }
        }

        return -1;
    }
}