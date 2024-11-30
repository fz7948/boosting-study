# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
# 설명: bfs 
# 시간: 12분 10초
# 난이도: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append((root, 0))
        visited = set()
        depth = {}

        while q:
            node, level = q.popleft()
            visited.add(node)
            if level not in depth:
                 depth[level] = []
            depth[level].append(node.val)

            if node.left and node.left not in visited:
                q.append((node.left, level+1))
            if node.right and node.right not in visited:
                q.append((node.right, level+1))
        
        ans = []
        for key in sorted(depth.keys()):
            if key %2 == 0:
                ans.append(depth[key])
            else:
                ans.append(depth[key][::-1])
        return ans
