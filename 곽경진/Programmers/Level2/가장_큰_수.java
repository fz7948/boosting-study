/*
프로그래머스 - 가장 큰 수 
https://school.programmers.co.kr/learn/courses/30/lessons/42746

    1. 정수 배열을 list 로 전환
    2. ab or ba 큰 값이 나오도록 정렬 
    3. 앞자리가 0일경우 0 return 

*/


import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
         String[] strNumbers = Arrays.stream(numbers)
                                     .mapToObj(String::valueOf)
                                     .toArray(String[]::new);

        Arrays.sort(strNumbers, (a, b) -> (b + a).compareTo(a + b));

        String result = String.join("", strNumbers);

        if (result.startsWith("0")) {
            return "0";
        }
        
        return result;
    }
}