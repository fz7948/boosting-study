class 올바른괄호 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=java
     */
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '(') stack.addLast(c);
            else {
                if (stack.isEmpty() || stack.peekLast() != '(')
                    return false;
                stack.pollLast();
            }
        }

        return stack.isEmpty();
    }
}