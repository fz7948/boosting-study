import java.util.PriorityQueue;

/*
    https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=java
    더 맵게

    주어진 리스트의 요소들이 K 보다 커야함.
    만족하지 못한다면 mix = (가장 작은 값 + (그다음 작은 값 *2))으로 새 값을 만듬.

    우선순위 큐를 만들고, 조건에 충족할 때까지 넣고 뺴고를 반복.


*/

class 더맵게 {

    public static void main(String[] args) {
        new 더맵게().solution(
                new int[]{1, 2, 3, 9, 10, 12}, 7
        );
    }
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int answer = 0;
       
        for (int i : scoville) {
            pq.add(i);
        }

        while (pq.size() > 1 && pq.peek() < K) {
            int mix = pq.poll() + (pq.poll() * 2);
            pq.add(mix);

            answer++;
        }

        return pq.peek() >= K ? answer : -1;
    }
}