# https://leetcode.com/problems/range-sum-of-bst/description/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        from collections import deque
        q = deque()
        q.append(root)
        ans = 0
        while q:
            
            node = q.popleft()

            if low <= node.val <=high:
                ans += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans