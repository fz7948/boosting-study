class 테이블해시함수 {

   /*
        https://school.programmers.co.kr/learn/courses/30/lessons/147354
        음 이건 1단계가 맞는거 같은데.
    */

    public int solution(int[][] data, int col, int row_begin, int row_end) {
        List<int[]> list = Arrays.stream(data).sorted((o1, o2) -> {
            if (o1[col - 1] == o2[col - 1]) return o2[0] - o1[0];
            else return o1[col - 1] - o2[col - 1];
        }).collect(Collectors.toList());

        List<Integer> integers = new ArrayList<>();
        for (int i = row_begin; i <= row_end; i++) {
            int temp = 0;
            for (int n : list.get(i-1)) {
                temp = temp + n % i;
            }

            integers.add(temp);
        }

        return integers.stream().reduce((integer, integer2) -> integer ^ integer2).get();
    }
}