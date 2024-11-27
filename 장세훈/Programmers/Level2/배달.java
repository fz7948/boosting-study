class 배달 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12978
        배달

        다이스트라 문제
    */
    public static void main(String[] args) {
        new 배달().solution(
                5,
                new int[][]{{1, 2, 1}, {2, 3, 3}, {5, 2, 2}, {1, 4, 2}, {5, 3, 1}, {5, 4, 2}},
                3
        );
    }

    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        int[] dists = new int[N + 1];
        Arrays.fill(dists, Integer.MAX_VALUE);
        Map<Integer, List<List<Integer>>> map = new HashMap<>();

        for (int[] r : road) {
            map.putIfAbsent(r[0], new ArrayList<>());
            map.putIfAbsent(r[1], new ArrayList<>());
            map.get(r[0]).add(List.of(r[1], r[2]));
            map.get(r[1]).add(List.of(r[0], r[2]));
        }

        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(Comparator.comparingInt(o1 -> o1.get(1)));
        pq.add(List.of(1, 0));

        while (!pq.isEmpty()) {
            List<Integer> poll = pq.poll();
            int to = poll.get(0);
            int dist = poll.get(1);

            if (dists[to] < dist) continue;
            dists[to] = dist;

            if (map.get(to) != null)
                for (List<Integer> node : map.get(to)) {
                    int newDist = node.get(1) + dist;

                    if (dists[node.get(0)] > newDist)
                        pq.add(List.of(node.get(0), newDist));
                }

        }


        for (int dist : dists) {
            if (dist <= K) answer++;
        }
        System.out.println(answer);
        return answer;
    }
}