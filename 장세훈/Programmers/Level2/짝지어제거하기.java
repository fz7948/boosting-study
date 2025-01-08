class 짝지어제거하기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12973
     */
    public int solution(String s) {
        Deque<Character> queue = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (queue.isEmpty() || queue.peekLast() != c)
                queue.addLast(c);
            else if (queue.peekLast() == c) {
                queue.pollLast();
            }
        }

        return queue.isEmpty() ? 1 : 0;
    }
}
