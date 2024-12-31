class 전력망을둘로나누기 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/86971?language=java
     */

    public int solution(int n, int[][] wires) {
        int answer = n;
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] wire : wires) {
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }

        for (int[] wire : wires) {
            int n1 = wire[0];
            int n2 = wire[1];

            graph.get(n1).remove(Integer.valueOf(n2));
            graph.get(n2).remove(Integer.valueOf(n1));

            boolean[] visit = new boolean[n + 1];
            int size1 = bfs(n1, graph, visit);
            int size2 = n - size1;

            answer = Math.min(answer, Math.abs(size1 - size2));

            graph.get(n1).add(n2);
            graph.get(n2).add(n1);
        }

        return answer;
    }

    int bfs(int start, List<List<Integer>> graph, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;
        int count = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            count++;

            for (int edge : graph.get(node)) {
                if (!visited[edge]) {
                    visited[edge] = true;
                    queue.add(edge);
                }
            }
        }

        return count;
    }

}