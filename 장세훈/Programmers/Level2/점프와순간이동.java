    class 점프와순간이동 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12980
     */

        public int solution(int n) {
            int answer = 0;

            while (n != 0) {
                if (n % 2 != 0)
                    answer++;
                n /= 2;
            }
            return answer;
        }
    }