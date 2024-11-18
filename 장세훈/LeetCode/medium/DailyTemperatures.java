import java.util.*;


class DailyTemperatures {
    /*
        hhttps://leetcode.com/problems/daily-temperatures/description/
        739. Daily Temperatures

        (프로그래머스에서 주식으로 비슷한 문제 풀었던거 같은데..)
        인덱스를 저장하는 stack을 준비한다
        배열을 순회하면서 현재 온도가 스택의 top보다 높으면 pop을 하고 날짜를 계산해 answer에 넣는다.
     */


    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> stack = new ArrayDeque<>();
        int[] answer = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.getLast()] < temperatures[i]) {
                Integer pop = stack.pollLast();
                answer[pop] = i - pop;
            }

            stack.add(i);
        }

        return answer;
    }
}