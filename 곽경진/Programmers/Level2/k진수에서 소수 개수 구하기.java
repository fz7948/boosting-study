/*
k진수에서 소수 개수 구하기 
https://school.programmers.co.kr/learn/courses/30/lessons/92335

    1. 양의정수 n을 k진수로 변환
    2. 그 숫자에서 0을 제거 후 for문을 돌리며 prime number 찾기 

*/


class Solution {
    public int solution(int n, int k) {        
        int answer = 0;
        String result = convert(n, k);
        
        String[] numbers = result.split("0");
        
        for(String number : numbers){
            if(!number.isEmpty()&&isPrime(number)) answer++;
        }
        return answer;
    }
    
    public String convert(int n, int k){
        String result = "";
        while(true){
            int x = n % k;
            result = x + result;
            n = n/k;
            if(n == 0) break;
        }
        return result;
    }
    public boolean isPrime(String s) {
        Long n = Long.valueOf(s);
        
        if (n <= 1) return false; 

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false; 
            }
        }
        return true; 
    }
}