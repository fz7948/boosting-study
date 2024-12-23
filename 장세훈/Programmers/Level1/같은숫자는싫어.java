class 같은숫자는싫어 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=java
     */

    public int[] solution(int[] arr) {
        Deque<Integer> queue = new ArrayDeque<>();

        for (int i : arr) {
            if(queue.isEmpty() || queue.peekLast() != i)
                queue.addLast(i);
        }

        return queue.stream().mapToInt(Integer::intValue).toArray();
    }
}