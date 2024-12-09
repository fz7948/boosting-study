class MinimumDistanceBetweenBSTNodes {

    /*
        https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
        783. Minimum Distance Between BST Nodes

        노드의 차가 가장 작은 값 구하기
        BST이므로 중위 탐색을 하면 정렬된 리스트를 구할 수 있음
        리스트를 순회해 차가 가장 적은 값 추출
     */

    List<Integer> list = new ArrayList<>();

    public int minDiffInBST(TreeNode root) {
        int minimum = Integer.MAX_VALUE;
        dfs(root);
        for (int i = 0; i < list.size() - 1; i++) {
            minimum = Math.min(list.get(i + 1) - list.get(i), minimum);
        }

        return minimum;
    }

    void dfs(TreeNode node) {
        if (node == null) return;

        dfs(node.left);
        list.add(node.val);
        dfs(node.right);
    }
}