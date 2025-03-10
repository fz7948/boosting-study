class CourseScheduleII {
    /*
        https://leetcode.com/problems/course-schedule-ii/
     */
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] count = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[1]).add(prerequisite[0]);
            count[prerequisite[1]]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < count.length; i++) {
            if (count[i] == 0)
                queue.add(i);
        }

        List<Integer> order = new ArrayList<>();

        while (!queue.isEmpty()) {
            Integer poll = queue.pollFirst();
            order.add(poll);

            for (Integer next : graph.get(poll)) {
                count[next]--;
                if (count[next] == 0)
                    queue.add(next);
            }

        }

        if (order.size() != numCourses)
            return new int[]{0};
        else
            return order.stream().mapToInt(Integer::intValue).toArray();
    }
}