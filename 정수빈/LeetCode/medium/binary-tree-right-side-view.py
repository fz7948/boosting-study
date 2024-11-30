# https://leetcode.com/problems/binary-tree-right-side-view
# 시간: 7분
# 설명: bfs
# 난이도: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append((root, 0))
        visited = set()
        depth = {}
        depth[0] = [root.val]

        while q:
            node, level = q.popleft()
            visited.add(node)
            if level not in depth:
                depth[level] = []
            depth[level].append(node.val)

            if node.left and not node.left in visited:
                q.append((node.left, level +1))
            if node.right and not node.right in visited:
                q.append((node.right, level +1))
        
        print(depth)
        ans = []
        for k in sorted(depth.keys()):
            ans.append(depth[k][-1])
        return ans
