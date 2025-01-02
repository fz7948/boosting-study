class 모음사전 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/84512
    */

    int answer = 0;
    int count = 0;

    public int solution(String word) {
        char[] alphabet = {'A', 'E', 'I', 'O', 'U'};
        dfs(alphabet, word, new StringBuilder());
        return answer;
    }

    void dfs(char[] alphabet, String word, StringBuilder now) {
        if (now.length() > 5 || answer != 0) return;
        if(word.contentEquals(now)) {
            answer =count;
            return;
        }

        for (char c : alphabet) {
            if(now.length() < 5) {
                count++;
                dfs(alphabet, word, now.append(c));
                now.deleteCharAt(now.length()-1);
            }
        }
    }
}