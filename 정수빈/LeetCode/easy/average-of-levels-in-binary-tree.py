# https://leetcode.com/problems/average-of-levels-in-binary-tree
# 시간: 7분 40초
# 설명: bfs
# 난이도: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = collections.deque()
        q.append((root, 0))
        visitied = set()

        output = {}
        count = {}
        while q:
            node, level = q.popleft()
            if node == None:
                continue
            visitied.add((node, level))
            if not level in output:
                output[level] = 0
                count[level] = 0
            output[level] += node.val
            count[level] += 1

            if not node.left in visitied:
                q.append((node.left, level + 1))
            if not node.right in visitied:
                q.append((node.right, level + 1))
        
        ans = []
        for key in output.keys():
            ans.append(output[key] / count[key])
        return ans
            
        