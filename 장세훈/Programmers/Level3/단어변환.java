class 단어변환 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=java
    */
    int answer = Integer.MAX_VALUE;
    boolean[] visit;

    public static void main(String[] args) {
        System.out.println(new 단어변환().solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log", "cog"}));
    }

    public int solution(String begin, String target, String[] words) {
        visit = new boolean[words.length];
        dfs(begin, target, words, 0);
        return answer == Integer.MAX_VALUE ? 0 : answer;
    }

    void dfs(String begin, String target, String[] words, int count) {
        if (begin.equals(target)) {
            answer = Math.min(count, answer);
        }

        for (int i = 0; i < words.length; i++) {
            if (!visit[i] && canChange(begin, words[i])) {
                visit[i] = true;
                dfs(words[i], target, words, count + 1);
                visit[i] = false;
            }
        }

    }

    boolean canChange(String s1, String s2) {
        int cnt = 0;

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == s2.charAt(i)) cnt++;
        }
        return cnt == 1;
    }
}