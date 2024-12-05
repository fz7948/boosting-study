/*
프로그래머스 괄호 회전 시키기
https://school.programmers.co.kr/learn/courses/30/lessons/76502

해야할 것
1. 올바른 괄호문자열인지 확인하기 -> '}]) 가 먼저 나온다면, 올바른 괄호문자열이 아님'
2. string 값 회전시키기

    1. string 값을 length 만큼 반복시키며 마지막 문자열이 맨 앞으로 오게 만듦
    2. 올바른 괄호 문자열인지 확인
        2-1. 올바른 문자열이면 +1
        2-2. 아니라면 계속진행
*/
import java.util.Stack;

class Solution {
    public int solution(String s) {
        
        int answer = 0;
        
        if (s.length()%2 == 1 || !parenthesesSet(s)){
            return 0;
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (parenthesesCheck(s)) {
                answer++;
            }
            s = stringShift(s);
        }
        
        return answer;
    }
    
    public String stringShift(String str) {
        return str.substring(1) + str.charAt(0);
    }
    
    public boolean parenthesesCheck(String str){
        Stack<Character> stack = new Stack<>();

        for (char ch : str.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }
            else if (ch == ')' || ch == '}' || ch == ']') {
                if (stack.isEmpty()) {
                    return false;
                }
                char openBracket = stack.pop();
                if (!isMatchingPair(openBracket, ch)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
    
     private static boolean isMatchingPair(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '{' && close == '}') ||
               (open == '[' && close == ']');
    }
    
    public boolean parenthesesSet(String str) {
    return str.chars().filter(c -> c == '(').count() == str.chars().filter(c -> c == ')').count()
        && str.chars().filter(c -> c == '{').count() == str.chars().filter(c -> c == '}').count()
        && str.chars().filter(c -> c == '[').count() == str.chars().filter(c -> c == ']').count();
    }
}
