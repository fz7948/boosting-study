class 땅따먹기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12913
     */
    int solution(int[][] land) {
        int[][] arr = new int[land.length][4];
        arr[0][0] = land[0][0];
        arr[0][1] = land[0][1];
        arr[0][2] = land[0][2];
        arr[0][3] = land[0][3];


        for (int i = 1; i < land.length; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (j == k) continue;
                    arr[i][j] = Math.max(arr[i][j], land[i][j] + arr[i - 1][k]);
                }
            }
        }

        return Arrays.stream(arr[land.length - 1]).max().getAsInt();
    }
}
