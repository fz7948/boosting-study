class PathSum {
    /*
        112. Path Sum
        https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

        tree의 root에서 leaf까지의 경로의 합이 targetSum와 같은게 있다면 true 반환
    */
    public static void main(String[] args) {
        new PathSum().hasPathSum(
                new TreeNode(1, new TreeNode(2), null), 1
        );
    }

    boolean answer = false;

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        dfs(root, targetSum, 0);
        return answer;
    }

    void dfs(TreeNode node, int targetSum, int sum) {
        if (answer) return;
        if (node != null)
            sum += node.val;

        if (node.right == null && node.left == null) {
            if (sum == targetSum)
                answer = true;
            return;
        }

        if(node.left != null) dfs(node.left, targetSum, sum);
        if(node.right != null) dfs(node.right, targetSum, sum);
    }
}