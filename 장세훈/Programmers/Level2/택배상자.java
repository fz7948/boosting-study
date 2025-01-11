class 택배상자 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/131704
     */
    public int solution(int[] order) {
        int answer = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        int orderIndex = 0;

        for (int i = 1; i <= order.length; i++) {
            stack.addLast(i);

            while (!stack.isEmpty() && order[orderIndex] == stack.peekLast()) {
                stack.pollLast();
                answer++;
                orderIndex++;
            }
        }

        return answer;
    }
}