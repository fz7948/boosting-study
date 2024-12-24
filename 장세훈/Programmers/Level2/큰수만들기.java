class 큰수만들기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=java
        그리디 문제
        스택에 숫자를 넣기 전에, 스택의 이전 숫자가 작다면 pop
    */
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : number.toCharArray()) {
            while (!stack.isEmpty() && Integer.parseInt(stack.peekLast() + "") < Integer.parseInt(c + "") && k != 0) {
                stack.pollLast();
                k--;
            }
            stack.addLast(c);
        }

        for (Character c : stack) {
            answer.append(c);
        }

        return k != 0 ? answer.substring(0, answer.length() - k) : answer.toString();
    }
}