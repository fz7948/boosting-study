# https://leetcode.com/problems/binary-tree-preorder-traversal/description/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        def dfs(node):
            if not node:
                return 
            
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ans