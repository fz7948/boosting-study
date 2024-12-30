class 카펫 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=java

        x * y = b + y
        b = (x+y) * 2 - 4
     */
    public int[] solution(int brown, int yellow) {
        int[] answer = {};

        for (int i = 1; i < 5000; i++) {
            for (int j = 1; j < 5000; j++) {
                if (i * j == brown + yellow && brown == (i + j) * 2 - 4) {
                    if (i > j)
                        return new int[]{i, j};
                    else
                        return new int[]{j, i};
                }
            }
        }

        return answer;
    }
}