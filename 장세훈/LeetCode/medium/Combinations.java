import java.util.*;

class Combinations {
    /*
        77. Combinations
        https://leetcode.com/problems/combinations/description/
     */

    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        dfs(n, k, new ArrayList<>(), 1);
        return answer;
    }

    void dfs(int n, int k, List<Integer> list, int start) {
        if (list.size() == k) {
            answer.add(List.copyOf(list));
            return;
        }

        for (int i = start; i <= n; i++) {
            list.add(i);
            dfs(n, k, list, i + 1);
            list.removeLast();
        }
    }
}