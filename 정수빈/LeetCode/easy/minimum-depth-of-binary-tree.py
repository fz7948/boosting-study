# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque

        q = deque()
        q.append((root, 0))
        ans = float("inf")

        if root == None:
            return 0
        
        while q:
            node, count = q.popleft()

            if node.left:
                q.append((node.left, count+1))
            if node.right:
                q.append((node.right, count+1))
            
            if not node.left and not node.right:
                ans = min(ans, count+1)
        return ans