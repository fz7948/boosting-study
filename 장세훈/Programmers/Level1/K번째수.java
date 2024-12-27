class K번째수 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=java
    */
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();

        for (int[] command : commands) {
            List<Integer> list = new ArrayList<>();

            for (int i = command[0]-1; i < command[1]; i++) {
                list.add(array[i]);
            }
            answer.add(list.stream().sorted().mapToInt(Integer::intValue).toArray()[command[2]-1]);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
