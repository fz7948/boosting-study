class 체육복 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=java

     */

    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] arr = new int[n + 1];

        for (int i : reserve) arr[i]++;
        for (int i : lost) arr[i]--;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == -1 && i - 1 > 0 && arr[i - 1] > 0) {
                arr[i]++;
                arr[i - 1]--;
            } else if (arr[i] == -1 && i + 1 < n + 1 && arr[i + 1] > 0) {
                arr[i]++;
                arr[i + 1]--;
            }
        }

        for (int i : arr) {
            if (i > -1)
                answer++;
        }
        return answer - 1;
    }
}