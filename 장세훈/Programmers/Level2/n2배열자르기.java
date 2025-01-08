class n2배열자르기 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/87390
     */

    public int[] solution(int n, long left, long right) {
        long[] from = new long[]{left / n, left % n};
        long[] to = new long[]{right / n, right % n};

        List<Long> list = new ArrayList<>();
        while (from[0] <= to[0] && from[1] <= to[1]) {
            list.add(Math.max(from[0], from[1]) + 1);

            if (from[1] + 1 == n) {
                from[0]++;
            }

            from[1] = (from[1] + 1) % n;
        }

        list.add(Math.max(from[0], from[1]) + 1);
        return list.stream().mapToInt(Long::intValue).toArray();
    }
}