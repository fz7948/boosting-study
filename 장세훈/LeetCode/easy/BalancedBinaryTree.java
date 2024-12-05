class BalancedBinaryTree {
    /*
        110. Balanced Binary Tree
        https://leetcode.com/problems/balanced-binary-tree/description/

        주어진 트리가 높이 균형인지 판별하는 문제.
        높이 균형이란 자식 노드들의 높이 차가 1 이하 인 것을 의미
        dfs로 해당 노드의 왼쪽 자식 노드 높이와 오른쪽 자식 노드 높이의 차를 구함.
     */

    boolean result = true;

    public boolean isBalanced(TreeNode root) {
        dfs(root, 0);
        return result;
    }

    int dfs(TreeNode node, int depth) {
        if (node == null || !result) return depth;

        int left = dfs(node.left, depth + 1);
        int right = dfs(node.right, depth + 1);

        if (Math.abs(left - right) > 1)
            result = false;

        return Math.max(left, right);
    }
}