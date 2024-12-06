class RangeSumBST {
    /*
        938. Range Sum of BST
        https://leetcode.com/problems/range-sum-of-bst/description/

        BST(이진 탐색 트리) 탐색 문제.
        문제는 브루트 포스로 풀리긴 헀으나, 이진 탐색 트리의 특성에 따라 최적화 시키는 방법이 있었음.
     */

    int result = 0;

    public int rangeSumBST(TreeNode root, int low, int high) {
        dfs(root, low, high);
        return result;
    }

    void dfs(TreeNode node, int low, int high) {
        if (node == null) return;

        if (node.val >= low && node.val <= high)
            result += node.val;

        dfs(node.left, low, high);
        dfs(node.right, low, high);
    }
}