class 행렬의곱셈 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12949
     */
    public int[][] solution(int[][] arr1, int[][] arr2) {
        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < arr1.length; i++) {
            List<Integer> list = new ArrayList<>();

            for (int j = 0; j < arr2[0].length; j++) {
                int a = 0;
                for (int k = 0; k < arr2.length; k++) {
                    a += arr1[i][k] * arr2[k][j];
                }
                list.add(a);
            }
            answer.add(list);
        }

        return answer.stream()
                .map(row -> row.stream().mapToInt(Integer::intValue).toArray())
                .toArray(int[][]::new);
    }
}