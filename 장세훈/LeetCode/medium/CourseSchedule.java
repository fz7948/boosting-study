class CourseSchedule {
    /*
        207. Course Schedule
        https://leetcode.com/problems/course-schedule/description/

        그래프가 순환 구조인지 판별하는 문제 (해설을 봐도 어렵군요...)

        완료해야 하는 노드(finish)가 처리해야 하는 노드(takes)에 포함되어 있다면 순환 구조
         - [1] -> [0],  [0] -> [1]
        처리해야하는 노드와 처리한 노드를 저장하는 리스트를 만들어 관리


     */

    public static void main(String[] args) {
        System.out.println( new CourseSchedule().canFinish(2, new int[][]{
                {1, 0}, {0, 1}
        }));
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> finishToTakeMap = new HashMap<>();

        for (int[] prerequisite : prerequisites) {
            finishToTakeMap.putIfAbsent(prerequisite[0], new ArrayList<>());
            finishToTakeMap.get(prerequisite[0]).add(prerequisite[1]);
        }

        // 처리해야 하는 노드 저장
        List<Integer> takes = new ArrayList<>();
        // 처리한 노드 저장
        List<Integer> taken = new ArrayList<>();

        for (Integer finish : finishToTakeMap.keySet()) {
            if (!dfs(finishToTakeMap, finish, takes, taken))
                return false;
        }

        return true;
    }

    boolean dfs(Map<Integer, List<Integer>> finishToTakeMap, Integer finish, List<Integer> takes, List<Integer> taken) {
        if (takes.contains(finish)) return false;   // 그래프가 순환 구조이므로 false
        if (taken.contains(finish)) return true;     // 이미 처리한 노드 리턴

        if (finishToTakeMap.containsKey(finish)) {
            takes.add(finish);

            for (Integer take : finishToTakeMap.get(finish)) {
                if (!dfs(finishToTakeMap, take, takes, taken))
                    return false;
            }

            takes.remove(finish);
            taken.add(finish);
        }

        return true;
    }

}