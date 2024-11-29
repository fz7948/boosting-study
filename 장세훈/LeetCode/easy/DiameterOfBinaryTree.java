class DiameterOfBinaryTree {
    /*
        543. Diameter of Binary Tree
        https://leetcode.com/problems/diameter-of-binary-tree/description/

        이진 트리의 노드간 가장 멀리 있는 길이
        왼쪽 노드의 깊이와 오른쪽 노드의 깊이의 합이 가장 큰 값을 찾아내는 문제
     */

    int answer = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return answer;
    }

    int dfs(TreeNode node) {
        if (node == null) return -1;
        int left = dfs(node.left);
        int right = dfs(node.right);

        answer = Math.max(left + right + 2, answer);

        return Math.max(left, right) + 1;
    }

}