# https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150
# 난이도: easy
# 시간: 14분

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.answer = False
        def dfs(node, total):
            if node.right == None and node.left == None and total == targetSum:
                self.answer = True
                return 
            
            if node.left:
                dfs(node.left, total + node.left.val)
            if node.right:
                dfs(node.right, total + node.right.val)
        if root:
            dfs(root, root.val)
            
        return self.answer