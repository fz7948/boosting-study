class 최소직사각형 {
    /*
         https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=java
     */

    public int solution(int[][] sizes) {
        int n1 = 0, n2 = 0;
        for (int[] size : sizes) {
            if (size[0] > size[1]) {
                n1 = Math.max(n1, size[0]);
                n2 = Math.max(n2, size[1]);
            } else {
                n1 = Math.max(n1, size[1]);
                n2 = Math.max(n2, size[0]);
            }
        }
        return n1 * n2;
    }
}