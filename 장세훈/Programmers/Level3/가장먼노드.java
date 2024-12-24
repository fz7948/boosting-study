class 가장먼노드 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=java
        그래프 거리 구하기
     */

    public int solution(int n, int[][] edge) {
        int answer = 0;
        int[] dists = new int[n];
        Arrays.fill(dists, Integer.MAX_VALUE);

        Map<Integer, List<Integer>> graph = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(n2 -> n2[1]));

        for (int[] ints : edge) {
            graph.putIfAbsent(ints[0] - 1, new ArrayList<>());
            graph.putIfAbsent(ints[1] - 1, new ArrayList<>());
            graph.get(ints[0] - 1).add(ints[1] - 1);
            graph.get(ints[1] - 1).add(ints[0] - 1);
        }

        pq.add(new int[]{0, 0});

        int max = -1;

        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int node = poll[0];
            int dist = poll[1];
            max = Math.max(dist, max);

            if (dists[node] < dist) continue;
            dists[node] = dist;

            List<Integer> edges = graph.get(node);
            for (Integer i : edges) {
                if (dist + 1 < dists[i]) {
                    pq.add(new int[]{i, dist + 1});
                    dists[i] = dist + 1;
                }
            }

        }

        for (int dist : dists) {
            if (dist == max) answer++;
        }

        return answer;
    }
}