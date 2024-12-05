/*
프로그래머스 최솟값 만들기 
https://school.programmers.co.kr/learn/courses/30/lessons/12941

문제 해결방법 
최소값을 만들려면 가장큰값 * 가장작은갑이 되어야함

    1. AB 모두 오름차순 정렬함
    3. A는 앞에서 B는 뒤에서 곱하고 모두 더하기 

*/

import java.util.Arrays;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
   
        for ( int i = 0 ; i < A.length ; i++){
             answer += A[i] * B[B.length - i -1];
        }
        
        return answer;
    }
}