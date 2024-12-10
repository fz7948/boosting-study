/*
프로그래머스 피보나치의_수
https://school.programmers.co.kr/learn/courses/30/lessons/12945

    피보나치 수가 너무 커지는 것을 제한하기 위해서 1234567 의 나머지를 만들면서 진행 
*/
class Solution {
    public int solution(int n) {
        int MOD = 1234567;
        int a = 0; 
        int b = 1; 

        for (int i = 2; i <= n; i++) {
            int temp = (a + b) % MOD;
            a = b;
            b = temp;
        }

        return b;
    }
}