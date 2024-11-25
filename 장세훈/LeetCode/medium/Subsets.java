import java.util.*;

class Subsets {
    /*
        https://leetcode.com/problems/subsets/description/
        78.Subsets

        모든 부분집합을 구하는 문제
        모든 탐색 경로가 부분집합이 되므로 다른 조건없이 결과를 answer에 추가함

     */


    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        dfs(nums, new ArrayList<>(), 0);
        return answer;
    }

    void dfs(int[] nums, List<Integer> list, int start) {
        answer.add(List.copyOf(list));

        for (int i = start; i < nums.length; i++) {
            list.add(nums[i]);
            dfs(nums, list, i + 1);
            list.removeLast();
        }
    }
}