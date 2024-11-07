    /*
        괄호 회전하기
        https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=java

        문자열을 회전하면서 올바른 괄호 문자열인지 확인한다.
        올바른 괄호 여부는 스택으로 확인한다.
    */

public int solution(String s) {
        int answer = -1;

        for (int i = 0; i < s.length() + 1; i++) {
            String rotate = s.substring(i) + s.substring(0, i);
            if (isCorrect(rotate))
                answer++;
        }

        return answer;
    }

public boolean isCorrect(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '[' || c == '{')
            stack.push(c);
        else {
            if (stack.isEmpty()) return false;
            Character pop = stack.peek();
            if ((c == ')' && pop == '(') || (c == ']' && pop == '[') || (c == '}' && pop == '{'))
                stack.pop();
            else
                return false;
        }
    }

    return stack.isEmpty();
}