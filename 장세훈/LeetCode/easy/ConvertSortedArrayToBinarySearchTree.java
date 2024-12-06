class ConvertSortedArrayToBinarySearchTree {
    /*
        108. Convert Sorted Array to Binary Search Tree
        https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

        정렬된 배열을 이진 탐색 트리로 만들기
        배열의 중간 값을 추출해 노드로 만듬, 배열을 반으로 자르고 중간 값을 추출하는 작업 반복
     */
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) return null;
        return dfs(nums, 0, nums.length - 1);
    }

    TreeNode dfs(int[] nums, int left, int right) {
        if (left > right) return null;

        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[mid]);

        node.left = dfs(nums, left, mid - 1);
        node.right = dfs(nums, mid + 1, right);
        return node;
    }
}