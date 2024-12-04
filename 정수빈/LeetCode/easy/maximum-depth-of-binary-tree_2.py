# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150
# 설명: dfs, maximum-depth-of-binary-tree을 다시 풀어봄
# 난이도: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth):
            if node == None:
                return depth
            
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return dfs(root, 0)
            