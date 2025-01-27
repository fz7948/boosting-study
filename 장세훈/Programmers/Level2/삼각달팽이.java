class 삼각달팽이 {

   /*
        https://school.programmers.co.kr/learn/courses/30/lessons/68645
    */

    public int[] solution(int n) {
        int[][] arr = new int[n][n];
        int[][] d = new int[][]{{1, 0}, {0, 1}, {-1, -1}};
        int[] now = {0, 0};
        int dIndex = 0;
        int count = 1;

        if (n == 1) return new int[]{1};

        while (true) {
            if (arr[now[0]][now[1]] != 0) break;

            arr[now[0]][now[1]] = count++;

            int newX = d[dIndex][0] + now[0];
            int newY = d[dIndex][1] + now[1];
            if (newX >= n || newY >= n || newX < -1 || newY < -1 || arr[newX][newY] != 0) {
                dIndex = (dIndex + 1) % 3;
                now[0] = d[dIndex][0] + now[0];
                now[1] = d[dIndex][1] + now[1];
            } else {
                now[0] = newX;
                now[1] = newY;
            }
        }

        List<Integer> answer = new ArrayList<>();
        for (int[] ints : arr) {
            for (int anInt : ints) {
                if (anInt != 0)
                    answer.add(anInt);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}