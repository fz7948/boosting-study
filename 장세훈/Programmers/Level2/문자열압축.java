class 문자열압축 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/60057
     */

    public int solution(String s) {
        int answer = s.length();

        for (int i = 1; i <= s.length() / 2; i++) {
            String base = s.substring(0, i);
            String zip = "";
            int count = 1;
            int left = i;

            while (left + i <= s.length()) {
                String substring = s.substring(left, left + i);
                if (base.equals(substring))
                    count++;
                else {
                    zip = count == 1 ? zip + base : zip + count + base;
                    base = substring;
                    count = 1;
                }

                left += i;
            }

            zip = count == 1 ? zip + base + s.substring(left) : zip + count + base + s.substring(left);
            answer = Math.min(zip.length(), answer);
        }

        return answer;
    }
}