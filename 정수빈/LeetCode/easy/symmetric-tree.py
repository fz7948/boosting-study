# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
# 난이도: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetry(p, q):
            if p == None and q == None:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return symmetry(p.left, q.right) and symmetry(p.right, q.left) 
            else:
                return False
        
        return symmetry(root.left, root.right)