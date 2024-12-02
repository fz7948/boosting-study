class DiameterOfBinaryTree {
    /*
        543. Diameter of Binary Tree
        https://leetcode.com/problems/diameter-of-binary-tree/description/

        이진 트리의 노드간 가장 멀리 있는 길이
        왼쪽 노드의 깊이와 오른쪽 노드의 깊이의 합이 가장 큰 값을 찾아내는 문제
     */

    int diameter = 0; 

     int diameterOfBinaryTree(TreeNode root) {
        dfs(root); 
        return diameter; 
    }

     int dfs(TreeNode node) {
        if (node == null) return 0; 

        int leftDepth = dfs(node.left);
        int rightDepth = dfs(node.right);

        diameter = Math.max(diameter, leftDepth + rightDepth);

        return Math.max(leftDepth, rightDepth) + 1;
    }

}