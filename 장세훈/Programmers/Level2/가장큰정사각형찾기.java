class 가장큰정사각형찾기 {
    /*
            https://school.programmers.co.kr/learn/courses/30/lessons/12905
            dp 문제
            각각 board[i][j-1], board[i-1][j], board[i-1][j-1] 중에 0이 없다면 사각형의 크기는 저 중 최소값의 +1로 구할 수 있음
     */

    public int solution(int[][] board) {
        int answer = 0;

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 1) {
                    answer = Math.max(1, answer);

                    if (i > 0 && j > 0) {
                        int min = Math.min(board[i - 1][j], Math.min(board[i - 1][j - 1], board[i][j - 1]));

                        if (min != 0) {
                            board[i][j] = min + 1;
                            answer = Math.max((min + 1) * (min + 1), answer);
                        }
                    }
                }
            }
        }

        return answer;
    }
}