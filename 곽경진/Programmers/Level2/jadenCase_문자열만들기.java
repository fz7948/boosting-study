/*
프로그래머스 jadenCase_문자열만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
    1. 문자열 첫번째는 부터 대문자 만들어야 하므로 true 로 시작 
    2. 공백 문자 다음엔 대문자로 만들어야함 
    3. 아닐때는 소문자로 변경 
    
*/

class Solution {
    public String solution(String s) {
        StringBuilder result = new StringBuilder();
        boolean blank = true;

        for (char c : s.toCharArray()) {
            if (c == ' ') {
                result.append(c);
                blank = true; 
            } else if (blank) {
                result.append(Character.toUpperCase(c));
                blank = false; 
            } else { 
                result.append(Character.toLowerCase(c));
            }
        }
        return result.toString();
    }
}