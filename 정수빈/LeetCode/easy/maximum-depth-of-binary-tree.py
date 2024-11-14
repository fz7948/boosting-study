# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxH = 0

        def dfs(node, height):
            if node == None:
                return
            self.maxH = max(self.maxH, height)
            
            if node.left:
                dfs(node.left, height+1)
            if node.right:
                dfs(node.right, height+1)
        
        dfs(root, 1)
        return self.maxH
        