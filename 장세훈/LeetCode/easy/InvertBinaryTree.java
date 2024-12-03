class InvertBinaryTree {

    /*
        226. Invert Binary Tree
        https://leetcode.com/problems/invert-binary-tree/description/

        트리를 반전 시키는 문제
        dfs로 현재 노드의 자식 노드들을 스왑한다.

     */

    public TreeNode invertTree(TreeNode root) {
        dfs(root);
        return root;
    }

    void dfs(TreeNode node) {
        if (node == null) return;

        dfs(node.left);
        dfs(node.right);

        TreeNode temp = node.left;
        node.left = node.right;
        node.right = temp;
    }
}