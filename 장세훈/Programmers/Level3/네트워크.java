class 네트워크 {

    int answer = 0;
    boolean[] visit;

    public int solution(int n, int[][] computers) {
        visit = new boolean[computers.length];

        for (int i = 0; i < computers.length; i++) {
            if (!visit[i]) {
                dfs(i, computers);
                answer++;
            }
        }

        return answer;
    }

    void dfs(int index, int[][] computers) {
        visit[index] = true;

        for (int i = 0; i < computers[index].length; i++) {
            if (computers[index][i] == 1 && !visit[i]) {
                dfs(i, computers);
            }
        }
    }
}