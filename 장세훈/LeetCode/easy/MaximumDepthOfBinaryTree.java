class MaximumDepthOfBinaryTree {
    /*
        https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1465826004/
        104. Maximum Depth of Binary Tree

        이진 트리의 최대 깊이를 구하는 문제
        dfs로 자식 노드로 이동하면서 깊이 카운팅
     */

    public int maxDepth(TreeNode root) {
        return dfs(root);
    }

    int dfs(TreeNode node) {
        if (node == null) return 0;
        return Math.max(dfs(node.right), dfs(node.left)) + 1;
    }
}