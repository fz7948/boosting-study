class NetworkDelayTime {
    /*
        743. Network Delay Time
        https://leetcode.com/problems/network-delay-time/description/

        다이스트라 알고리즘
     */

    public static void main(String[] args) {
        new NetworkDelayTime().networkDelayTime(
                new int[][]{
                        {2, 1, 1}, {2, 3, 1,}, {3, 4, 1,}
                },
                4, 2
        );
    }

    public int networkDelayTime(int[][] times, int n, int k) {
        // map으로 graph 세팅
        Map<Integer, List<List<Integer>>> map = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int[] time : times) {
            map.get(time[0]).add(List.of(time[1], time[2]));
        }

        // k부터 다른 노드들 까지의 거리 저장
        int[] dists = new int[n + 1];
        Arrays.fill(dists, Integer.MAX_VALUE);

        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.get(1)));

        pq.add(List.of(k, 0));

        while (!pq.isEmpty()) {
            List<Integer> poll = pq.poll();
            int to = poll.get(0);
            int dist = poll.get(1);

            if (dists[to] < dist) continue;
            dists[to] = dist;

            for (List<Integer> nodes : map.get(to)) {
                int newDist = dist + nodes.get(1);

                if (dists[nodes.get(0)] > newDist) {
                    pq.add(List.of(nodes.get(0), newDist));
                }
            }
        }

        int answer = 0;
        for (int i = 1; i < dists.length; i++) {
            if (dists[i] == Integer.MAX_VALUE) return -1;
            answer = Math.max(answer, dists[i]);
        }

        return answer;
    }
}