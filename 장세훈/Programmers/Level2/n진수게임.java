class n진수게임 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/17687
     */
    public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();
        int num = 0;
        int turn = 0;

        while (answer.length() != t) {
            String string = Integer.toString(num, n).toUpperCase();
            for (char c : string.toCharArray()) {
                if (turn == p - 1) {
                    answer.append(c);
                }

                if (answer.length() == t)
                    return answer.toString();

                turn = (turn + 1) % m;
            }

            num++;
        }

        return answer.toString();
    }
}