/*
프로그래머스 문자열_내림차순_배치하기 

    1. String to CharArray 
    2. 정렬 
    3. StringBuilder 로 만들고 reverse 해서 역정렬 
*/
import java.util.*;

class Solution {
    public String solution(String s) {
        char[] answer = s.toCharArray();
        
        Arrays.sort(answer);
        
        StringBuilder sb = new StringBuilder(new String(answer));
        
        return sb.reverse().toString();
    }
}