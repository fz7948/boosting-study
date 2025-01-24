class 단속카메라 {

  /*
    https://school.programmers.co.kr/learn/courses/30/lessons/42884
   */

    public int solution(int[][] routes) {
        Arrays.sort(routes, (o1, o2) -> {
            if (o1[0] == o2[0])
                return o1[1] - o2[1];
            return o1[0] - o2[0];
        });

        int answer = 1;
        int left = routes[0][0];
        int right = routes[0][1];

        for (int[] route : routes) {
            if (route[0] >= left && route[0]  <= right) {
                left = Math.max(route[0],left);
                right = Math.min(route[1],right);
            }else {
                answer++;
                left = route[0];
                right = route[1];
            }

        }

        return answer;
    }
}