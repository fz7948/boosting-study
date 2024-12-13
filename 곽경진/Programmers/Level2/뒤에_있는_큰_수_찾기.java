/*
프로그래머스 뒤에_있는_큰_수_찾기
https://school.programmers.co.kr/learn/courses/30/lessons/154539

    1. 배열을 -1 로 초기화
    2. 스택에 뒤 큰수가 없는 인덱스 저장 
    3. 원소가 스택 맨 위에 있는 인덱스 값보다 크면, 큰 뒷수로 설정 
    4. ㅅ순회하면서 현재원소가 스택의 맨 위에 있는 원소보다 크면, 인덱스를 꺼내고 뒤 큰수를 현재원소로 설정
    5. 순회가 끝난 후 스택에 남아있는 원소는 뒷 큰수가 없으므로 -1 유지 
*/


import java.util.Stack;

class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<>();


        for (int i = 0; i < n; i++) {
            answer[i] = -1;
        }


        for (int i = 0; i < n; i++) {

            while (!stack.isEmpty() && numbers[stack.peek()] < numbers[i]) {
                int idx = stack.pop();
                answer[idx] = numbers[i];
            }

            stack.push(i);
        }

        return answer;
    }
}