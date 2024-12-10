/*
프로그래머스 짝지어_제거하기 
https://school.programmers.co.kr/learn/courses/30/lessons/12973
    스택 활용해서 char push & pop
    
*/


class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop(); 
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty() ? 1 : 0;
    }
}