# https://leetcode.com/problems/path-sum-ii/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        from collections import deque, defaultdict
        if not root:
            return []

        q = deque([(root, root.val, [root.val])])
        total_sum = defaultdict(list)

        while q:
            node, total, node_list = q.popleft()
            leaf = False
            if not node.left and not node.right:
                leaf = True
            if leaf:
                total_sum[total].append(node_list)

            if node.left:
                q.append((node.left, total+node.left.val, node_list + [node.left.val]))
            if node.right:
                q.append((node.right, total+node.right.val, node_list + [node.right.val]))
        return total_sum[targetSum]