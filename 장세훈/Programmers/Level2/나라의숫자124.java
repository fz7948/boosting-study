class 나라의숫자124 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12899
        해답봄..
     */

    public String solution(int n) {
        StringBuilder answer = new StringBuilder();
        String[] numbers = {"4", "1", "2"};

        while (n > 0) {
            int r = n % 3;
            n /= 3;
            if (r == 0) {
                n--;
            }
            answer.insert(0, numbers[r]);
        }

        return answer.toString();
    }
}