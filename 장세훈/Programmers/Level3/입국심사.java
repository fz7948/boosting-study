class 입국심사 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=java
        이분 검색으로 문제의 조건에 맞는 최소 값을 찾는 문제
        pass 값을 처음에 int로 선언해 overflow가 나서 삽질함
     */
    public long solution(int n, int[] times) {
        long left = 0, right = Long.MAX_VALUE;
        long answer = Long.MAX_VALUE;

        while (left <= right) {
            long mid = (left + right) / 2;

            long pass = 0;
            for (int time : times) {
                pass += (mid / time);
                if (pass >= n) break;
            }

            if (pass >= n) {
                answer = Math.min(answer, mid);
                right = mid - 1;
            } else
                left = mid + 1;
        }

        return answer;
    }
}