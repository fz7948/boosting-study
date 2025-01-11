class 뒤에있는큰수찾기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/154539
     */
    public int[] solution(int[] numbers) {
        Deque<Integer> stack = new ArrayDeque<>();
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);

        for (int i = 0; i < numbers.length; i++) {
            while (!stack.isEmpty() && numbers[stack.peekLast()] < numbers[i]) {
                answer[stack.pollLast()] = numbers[i];
            }

            stack.addLast(i);
        }

        return answer;
    }
}