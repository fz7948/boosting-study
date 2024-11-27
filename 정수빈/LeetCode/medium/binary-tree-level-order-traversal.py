# https://leetcode.com/problems/binary-tree-level-order-traversal
# 시간: 4분 40초
# 난이도: medium
# 설명: queue를 이용한 bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        visited = set()
        q.append((root, 0))
        depth = {}

        while q:
            node, level = q.popleft()
            visited.add(node)
            if level not in depth:
                depth[level] = []
            depth[level].append(node.val)

            if node.left and node.left not in visited:
                q.append((node.left, level+1) )
            if node.right and node.right not in visited:
                q.append((node.right, level+1))
        
        ans = []
        for key in sorted(depth.keys()):
            ans.append(depth[key])
        return ans

