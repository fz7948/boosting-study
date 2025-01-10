class k진수에서소수개수구하기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/92335
     */
    public static void main(String[] args) {
        System.out.println(new k진수에서소수개수구하기()
                .solution(110011, 10));
    }

    public int solution(int n, int k) {
        int answer = 0;

        String num = Integer.toString(n, k);
        String[] split = num.split("0");

        for (String s : split) {
            if (!s.isEmpty() && isPrime(Long.parseLong(s))) {
                answer++;
            }
        }
        return answer;
    }

    private boolean isPrime(long num) {
        if (num < 2) return false;
        for (long i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}