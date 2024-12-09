/*
프로그래머스 정수_삼각형 
https://school.programmers.co.kr/learn/courses/30/lessons/43105

    1. 최대값을 구하기 
    2. 아래부터 최대값을 구해야함 
*/

class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;

        for (int i = n - 2; i >= 0; i--) { 
            for (int j = 0; j <= i; j++) {        
                triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        
        return triangle[0][0];
    }
}