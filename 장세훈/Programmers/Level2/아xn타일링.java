class 아xn타일링 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12900
     */
    public int solution(int n) {
        int answer = 0;
        int a = 1;
        int b = 2;

        while (n - 2 != 0) {
            int temp = (a + b) % 1000000007;
            a = b;
            b = temp;
            n--;
        }

        return b;
    }
}