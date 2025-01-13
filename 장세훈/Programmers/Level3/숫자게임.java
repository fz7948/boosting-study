class 숫자게임 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12987
     */
    public int solution(int[] A, int[] B) {
        int answer = 0;
        int ap = 0, bp = 0;

        Arrays.sort(A);
        Arrays.sort(B);

        while (ap < A.length && bp < B.length) {
            if (A[ap] < B[bp]) {
                ap++;
                answer++;
            }
            bp++;
        }

        return answer;
    }
}