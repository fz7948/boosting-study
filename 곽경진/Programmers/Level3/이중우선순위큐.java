/*
프로그래머스 이중우선순위큐
https://school.programmers.co.kr/learn/courses/30/lessons/42628

    우선순위큐에 대한 공부 
    우선순위 큐는 각 요소에 우선순위를 부여하고 우선순위가 높은 요소가 먼저 삭제
    
    명령어에 의해서 삽입 or 삭제 진행 
    peek() : 우선순위가 가장 높은 요소를 반환합니다. (삭제 X)
    poll() : 우선순위가 가장 높은 요소를 반환하고 삭제합니다.
    
    
*/
import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (String operation : operations) {
            String[] parts = operation.split(" ");
            String command = parts[0];
            int value = Integer.parseInt(parts[1]);

            if (command.equals("I")) {
        
                minHeap.add(value);
                maxHeap.add(value);
            } else if (command.equals("D")) {
                if (!minHeap.isEmpty()) {
                    if (value == 1) {
         
                        int maxVal = maxHeap.poll();
                        minHeap.remove(maxVal);
                    } else if (value == -1) {
         
                        int minVal = minHeap.poll();
                        maxHeap.remove(minVal);
                    }
                }
            }
        }

        if (minHeap.isEmpty()) {
            return new int[]{0, 0};
        } else {
            return new int[]{maxHeap.peek(), minHeap.peek()};
        }
    }
}
