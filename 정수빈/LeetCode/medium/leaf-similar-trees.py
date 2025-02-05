# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root, leaves = []):
            visited = set()
            q = []
            q.append(root)
            while q:
                node = q.pop()
                visited.add(node)
                if node.left and not node.left in visited:
                    q.append(node.left)
                if node.right and not node.right in visited:
                    q.append(node.right)
                if not node.right and not node.left:
                    if node.right not in visited and node.left not in visited:
                        leaves.append(node.val)
            return leaves
        return dfs(root1, []) == dfs(root2, [])
            
