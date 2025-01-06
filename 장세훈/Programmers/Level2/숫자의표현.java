class 숫자의표현 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12924
     */

    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n + 1];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }

        int l = 1;
        int r = 1;
        int sum = 1;

        while (l <= r && l <= n && r <= n) {
            if (sum >= n) {
                if (sum == n) answer++;
                sum -= arr[l++];
            } else {
                sum += arr[++r];
            }
        }

        return answer;
    }
}