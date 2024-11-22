import java.util.*;

class CombinationSum {
    /*
        39.  Combination Sum
        https://leetcode.com/problems/combination-sum/description/
     */


    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        dfs(candidates, new ArrayList<>(), target, 0, 0);
        return answer;
    }

    void dfs(int[] candidates, List<Integer> list, int target, int sum, int start) {
        if (sum > target) return;
        if (sum == target) {
            answer.add(List.copyOf(list));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            list.add(candidates[i]);
            dfs(candidates, list, target, sum + candidates[i], i);
            list.removeLast();
        }
    }
}