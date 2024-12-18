class QueueReconstructionByHeight {

    /*
        https://leetcode.com/problems/queue-reconstruction-by-height/description/
        그리디 문제
        우선순위 큐, 키 오름차순, 순번 내림차순으로 정렬

     */

    public int[][] reconstructQueue(int[][] people) {
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0] ? b[0] - a[0] : a[1] - b[1]);
        List<int[]> result = new ArrayList<>();

        for (int[] person : people) {
            pq.add(person);
        }

        while (!pq.isEmpty()) {
            int[] person = pq.poll();
            result.add(person[1], person);
        }

        return result.toArray(new int[people.length][2]);
    }
}
