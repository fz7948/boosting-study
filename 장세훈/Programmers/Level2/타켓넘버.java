/*
    https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=java
    dfs 문제
    리스트의 요소를 덧셈 뺄셈하면서 탐색
*/

class Solution {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);

        return answer;
    }

    void dfs(int[] numbers, int target, int sum, int index) {
        if (numbers.length == index) {
            if (sum == target) answer++;
            return;
        }

        dfs(numbers, target, sum + numbers[index], index + 1);
        dfs(numbers, target, sum - numbers[index], index + 1);
    }
}