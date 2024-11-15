/*
        20. Valid Parentheses
        https://leetcode.com/problems/valid-parentheses/description/

        java는 Stack 대신 Dequq를 사용할 것을 권장.
        Stack은 모든 기능에 lock이 걸려 있어 성능상 안좋음
 */
class ValidParentheses {

    public static void main(String[] args) {
        new ValidParentheses().isValid("()");
    }
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> map = new HashMap<>() {{
            put(')', '(');
            put(']', '[');
            put('}', '{');
        }};

        for (char c : s.toCharArray()) {
            if(!map.containsKey(c)) {
                stack.push(c);
            }else if(stack.isEmpty() || stack.pop() != (map.get(c))) {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
