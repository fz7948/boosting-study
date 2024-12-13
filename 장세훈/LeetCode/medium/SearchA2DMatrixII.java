class SearchA2DMatrixII {
    /*
        https://leetcode.com/problems/search-a-2d-matrix-ii/
        
        2차원 배열에서 target값 유무 반환하는 문제
        행, 렬이 각각 오름차순으로 정렬되어 있어서 binarySearch 활용
     */

    public boolean searchMatrix(int[][] matrix, int target) {
        for (int[] ints : matrix) {
            if (ints[0] <= target) {
                int index = Arrays.binarySearch(ints, target);
                if (index > -1) return true;
            } else
                break;
        }
        return false;
    }
}