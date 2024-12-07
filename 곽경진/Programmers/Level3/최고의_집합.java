/*
프로그래머스 최고의_집합
https://school.programmers.co.kr/learn/courses/30/lessons/12938

    1. n < s 가되면 -1 반환 
    2. 최대값으로 만드려면 나눈 몫을 n만큼 분배 
    3. 나머지값을 뒤부터 1 씩 더하기
    
*/

class Solution {
    public int[] solution(int n, int s) {
        if (n < s) {
            return new int[]{-1};
        }
        int[] a = new int[n];
        
        int base = s / n;
        int remainder = s % n;

        int[] result = new int[n];
        Arrays.fill(result, base);

        for (int i = 0; i < remainder; i++) {
            result[n - 1 - i]++;
        }

        return result;
        
        
        int[] answer = {};
        return answer;
    }
}