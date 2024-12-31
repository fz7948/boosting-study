
class 피로도 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=java

     */

    int answer = -1;

    public int solution(int k, int[][] dungeons) {
        dfs(k, dungeons, new boolean[dungeons.length], 0);
        return answer;
    }

    void dfs(int k, int[][] dungeons, boolean[] visit, int count) {
        answer = Math.max(answer, count);

        for (int i = 0; i < dungeons.length; i++) {
            if (!visit[i] && dungeons[i][0] <= k && k-dungeons[i][1] >=0) {
                visit[i] = true;
                dfs(k - dungeons[i][1], dungeons, visit, count + 1);
                visit[i] = false;
            }
        }
    }
}