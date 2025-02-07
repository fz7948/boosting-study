class 가장긴팰린드롬 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12904
     */

    public int solution(String s) {
        int answer = 0;

        for (int i = 0; i < s.length(); i++) {
            int odd = getPalindromeLength(i, i, s);
            int even = getPalindromeLength(i, i + 1, s);

            answer = Math.max(Math.max(answer, odd), even);
        }

        return answer;
    }

    int getPalindromeLength(int left, int right, String s) {
        while (left > -1 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1;
    }

}