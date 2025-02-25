class FindingUsersActiveMinutes {

    /*
        https://leetcode.com/problems/finding-the-users-active-minutes/
     */

    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        int[] answer = new int[k];
        Map<Integer, Set<Integer>> map = new HashMap<>();

        for (int[] log : logs) {
            Set<Integer> orDefault = map.getOrDefault(log[0], new HashSet<>());
            orDefault.add(log[1]);
            map.put(log[0], orDefault);
        }

        for (Integer key : map.keySet()) {
            Set<Integer> integers = map.get(key);
            answer[integers.size() - 1]++;
        }

        for (int i : answer) {
            System.out.print(i + " ");
        }

        return answer;
    }
}