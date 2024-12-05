/*
프로그래머스 최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
    
    1. string 을 배열로 변경 
    2. 배열을 sort 
    3. 1번째 값은 가장 작은 값, 마지막 값은 가장큰 값 

*/
import java.util.Arrays;

class Solution {
    public String solution(String s) {
        
        String[] numbers = s.split(" ");
        
        
        int[] intNumbers = Arrays.stream(numbers)
                                  .mapToInt(Integer::parseInt)
                                  .toArray();
        Arrays.sort(intNumbers);
        
        return intNumbers[0] + " " + intNumbers[intNumbers.length - 1];
    }
}