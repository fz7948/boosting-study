class WordSearch {

  /*
      https://leetcode.com/problems/word-search/
   */

  boolean result = false;

  public boolean exist(char[][] board, String word) {
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        if (board[i][j] == word.charAt(0)) {
          boolean[][] visit = new boolean[board.length][board[0].length];
          visit[i][j] = true;
          dfs(board, word, visit, i, j, 0);
        }
      }
    }

    return result;
  }


  void dfs(char[][] board, String word, boolean[][] visit, int x, int y, int idx) {
    if (result) {
      return;
    }

    if (word.length() == (idx + 1)) {
      result = true;
      return;
    }

    int[][] dir = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    for (int[] d : dir) {
      int nx = x + d[0];
      int ny = y + d[1];

      if (nx > -1 && ny > -1 && nx < board.length && ny < board[0].length && !visit[nx][ny] && idx + 1 < word.length()
          && board[nx][ny] == word.charAt(idx + 1)) {
        visit[nx][ny] = true;
        dfs(board, word, visit, nx, ny, idx + 1);
        visit[nx][ny] = false;
      }
    }
  }

}