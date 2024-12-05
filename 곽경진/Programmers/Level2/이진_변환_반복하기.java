/*
이진 변환 반복하기 
https://school.programmers.co.kr/learn/courses/30/lessons/70129
    1. 0 과 1로 이루어진 문자열의 0을 모두제거 
    2. 그문자열의 0을 제거 
    3. 길이를 2진수로 변환
*/

class Solution {
    public int[] solution(String s) {
        int count = 0;
        int length = 0;
        while(true){
            int tempLength = s.length();
            String tempString = s.replace("0","");
            length += tempLength - tempString.length();
            count++;
            if(tempString.length() == 1){
                break;
            }
            s = Integer.toBinaryString(tempString.length());
        }
        int[] answer = {count,length};
        return answer;
    }
}