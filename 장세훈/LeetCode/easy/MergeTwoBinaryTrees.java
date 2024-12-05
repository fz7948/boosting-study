class MergeTwoBinaryTrees {
    /*
        617. Merge Two Binary Trees
        https://leetcode.com/problems/merge-two-binary-trees/description/

        dfs를 통해 두 트리를 합병
     */


    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        return dfs(root1, root2);
    }

    TreeNode dfs(TreeNode n1, TreeNode n2) {
        if (n1 == null && n2 == null) return null;

        int nv1 = n1 == null ? 0 : n1.val;
        int nv2 = n2 == null ? 0 : n2.val;

        TreeNode newNode = new TreeNode(nv1 + nv2);

        newNode.left = dfs((n1 == null || n1.left == null) ? null : n1.left, n2 == null || n2.left == null ? null : n2.left);
        newNode.right = dfs(n1 == null || n1.right == null ? null : n1.right, n2 == null || n2.right == null ? null : n2.right);

        return newNode;
    }
}