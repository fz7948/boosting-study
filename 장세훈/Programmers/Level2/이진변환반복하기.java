class 이진변환반복하기 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/70129
     */

    public int[] solution(String s) {
        int[] answer = new int[2];

        while (!s.equals("1")) {
            answer[0]++;
            answer[1] += s.length();
            s = s.replaceAll("0", "");
            answer[1] -= s.length();
            s = Integer.toBinaryString(s.length());
        }

        return answer;
    }
}
