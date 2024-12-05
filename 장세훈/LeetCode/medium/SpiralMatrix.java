class SpiralMatrix {
    /*
        https://leetcode.com/problems/spiral-matrix/
        54. Spiral Matrix

        이차원 배열을 나선형으로 탐색
     */

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int[][] direct = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int index = 0;
        int x = 0, y = 0;

        while (result.size() != matrix.length * matrix[0].length) {
            result.add(matrix[x][y]);
            matrix[x][y] = -101;

            int nx = x + direct[index][0];
            int ny = y + direct[index][1];

            if (nx < 0 || nx >= matrix.length || ny < 0 || ny > matrix[0].length || matrix[nx][ny] == -101) {
                index = (index + 1) % 4;
                nx = x + direct[index][0];
                ny = y + direct[index][1];
            }

            x = nx;
            y = ny;
        }

        return result;
    }
}