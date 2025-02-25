class IsValidSudoku {

   /*
        https://leetcode.com/problems/valid-sudoku/
    */

    public boolean isValidSudoku(char[][] board) {

        for (int i = 0; i < board.length; i++) {
            Set<Character> set1 = new HashSet<>();
            Set<Character> set2 = new HashSet<>();

            for (int j = 0; j < board.length; j++) {
                if ((board[i][j] != '.' && set1.contains(board[i][j])) || (board[j][i] != '.' && set2.contains(board[j][i]))) {
                    return false;
                } else {
                    set1.add(board[i][j]);
                    set2.add(board[j][i]);
                }
            }
        }
        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < board.length; j += 3) {
                Set<Character> set = new HashSet<>();
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        if (board[k][l] != '.' && set.contains(board[k][l])) {
                            return false;
                        } else
                            set.add(board[k][l]);
                    }
                }
            }
        }

        return true;
    }
}