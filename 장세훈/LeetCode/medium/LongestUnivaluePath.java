class LongestUnivaluePath {
    /*
        687. Longest Univalue Path
        https://leetcode.com/problems/longest-univalue-path/description/

        동일한 값을 가진 노드로 이루어진 가장 긴 길이 구하기

        dfs로 현재 node에서 값이 동일한 자식 노드의 길이를 반환
     */

    int result = 0;

    public int longestUnivaluePath(TreeNode root) {
        dfs(root);
        return result;
    }

    int dfs(TreeNode node) {
        if (node == null) return 0;

        int left = dfs(node.left);
        int right = dfs(node.right);

        if (node.left != null && node.left.val == node.val) left += 1;
        else left = 0;

        if (node.right != null && node.right.val == node.val) right += 1;
        else right = 0;

        result =  Math.max(result, left+right);

        return Math.max(left, right);
    }

}