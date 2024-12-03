# https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
# 설명: binary tree 기초 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if node == None:
                return 
            
            node_left = node.left
            node.left = node.right
            node.right = node_left

            invert(node.left)
            invert(node.right)

        invert(root)
        return root