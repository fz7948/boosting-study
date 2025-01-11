# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/?envType=problem-list-v2&envId=breadth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        value_list = set()

        def dfs(root):
            if root == None:
                return False
            
            for v in value_list:
                if v + root.val == k:
                    return True
            value_list.add(root.val)
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)