class Permutations {
    /*
        https://leetcode.com/problems/permutations/description/
        46. Permutations

        주어진 숫자들로 만들 수 있는 모든 순열을 만드는 문제
        dfs로 완전탐색하며 모든 조합을 만든다.
        visit를 통해 현재 숫자의 사용 여부를 저장한다.
     */


    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        boolean[] visit = new boolean[nums.length];
        dfs(nums, new ArrayList<>(), visit);
        return answer;
    }

    void dfs(int[] nums, List<Integer> list, boolean[] visit) {
        if (list.size() == nums.length) {
            answer.add(new ArrayList<>(list));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!visit[i]) {
                visit[i] = true;
                list.add(nums[i]);
                dfs(nums, list, visit);
                list.removeLast();
                visit[i] = false;
            }
        }
    }
}