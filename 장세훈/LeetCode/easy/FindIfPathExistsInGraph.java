class FindIfPathExistsInGraph {
    /*
        https://leetcode.com/problems/find-if-path-exists-in-graph/
     */
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visit = new boolean[n];
        visit[source] = true;
        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(source);

        while (!queue.isEmpty()) {
            int poll = queue.pollFirst();

            if (poll == destination) return true;

            for (int next : graph.get(poll)) {
                if (!visit[next]) {
                    visit[next] = true;
                    queue.add(next);
                }
            }
        }

        return visit[destination];
    }
}