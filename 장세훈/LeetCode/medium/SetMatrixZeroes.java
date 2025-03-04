class SetMatrixZeroes {

    /*
        https://leetcode.com/problems/set-matrix-zeroes/
     */
    public void setZeroes(int[][] matrix) {
        Set<int[]> set = new HashSet<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    set.add(new int[]{i, j});
                }
            }
        }

        for (int[] p : set) {
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][p[1]] = 0;
            }

            for (int i = 0; i < matrix[0].length; i++) {
                matrix[p[0]][i] = 0;
            }
        }
    }
}