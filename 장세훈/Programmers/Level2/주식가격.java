import java.util.*;

class 주식가격 {
    /*
        주식가격
        https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=java

        O(N^2)으로 풀면 효율성에서 탈락
        Stack을 활용해 O(N)으로 풀이

     */
    public int[] solution(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[prices.length];
        int i = 0;

        stack.add(i);
        for (i = 1; i < prices.length; i++) {
            while (!stack.empty() && prices[i] < prices[stack.peek()]) {
                int index = stack.pop();
                answer[index] = i - index ;
            }
            stack.add(i);
        }

        while (!stack.empty()) {
            int index = stack.pop();
            answer[index] = i - index - 1;
        }

        return answer;
    }

}