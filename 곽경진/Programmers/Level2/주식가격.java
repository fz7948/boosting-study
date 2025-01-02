
/*
프로그래머스 주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584

    1. stack 을 초기화 (여기에 가격이 떨어지지 않은 기간을 담을것)
    2. pirce 의 길이만 큼 시간이 흐름 -> 반복문
    3. stack 이 비어있지 않고 가격이 떨어졌다면 pop 후 현재시간에서 빼서 기록
    4. 아니라면 현재시간 push 
    5. 스택이 남아있으면 가격이 떨어지지 않은것 

*/

import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int idx = stack.pop();
                answer[idx] = i - idx;
            }
            stack.push(i);
        }
        
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            answer[idx] = n - 1 - idx; 
        }
        
        return answer;
    }
}