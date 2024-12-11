/*
프로그래머스 다리를_지나는_트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
    1. 다리를 0인 큐로 초기화 시킴
    2. 다리의 무게가 0 보다 크거나 트럭 갯수만큼 반복문실행
    3. 한번 지나갈때마다 time은 1 씩증가 
    4. 다리무게만큼 버틸수 있는 트럭만 받음 
    5. 만약에 다리무게가 버틸수 없다면 큐에 0만 추가 (시간만 흐르게)
    6. 반복문이 끝난 후의 time 반환 

*/


import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridgeLength, int weight, int[] truckWeights) {
        Queue<Integer> bridge = new LinkedList<>();
        int time = 0;
        int bridgeWeight = 0;
        int index = 0;

        for (int i = 0; i < bridgeLength; i++) {
            bridge.offer(0);
        }

        while (index < truckWeights.length || bridgeWeight > 0) {
            time++; 
            bridgeWeight -= bridge.poll();            
            if (index < truckWeights.length && bridgeWeight + truckWeights[index] <= weight) {
                bridge.offer(truckWeights[index]);
                bridgeWeight += truckWeights[index];
                index++;
            } else {
                bridge.offer(0);
            }
        }

        return time;
    }
}