# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# 설명: bfs
# 난이도: medium
# 시간: 19분

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = set()
        output_dict = {}

        ans = []
        queue = [(root, 0)]
        while queue:
            node, idx = queue.pop(0)
            if node == None:
                continue

            visited.add(node)
            if not idx in output_dict:
                output_dict[idx] = []
            output_dict[idx].append(node.val)

            if not node.left in visited:
                queue.append((node.left, idx-1))
            if not node.right in visited:
                queue.append((node.right, idx+1))
        
        keys = sorted(output_dict.keys())
        for key in keys:
            ans.append(output_dict[key])
        return ans
        
        