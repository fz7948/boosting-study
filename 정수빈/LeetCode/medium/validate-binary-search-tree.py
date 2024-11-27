# https://leetcode.com/problems/validate-binary-search-tree
# 설명: bfs로 bst가 올바른지 체크
# 난이도: medium
# 시간: 40분정도 걸린듯? 아이디어는 괜찮았지만, 마지막에 어캐해야할지 몰라서 지피티한테 물어봄..ㅠ

import collections
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = collections.deque()
        q.append((root, float("-inf"), float("inf")))

        while q:
            node, min_val, max_val = q.popleft()

            # If the current node's value violates the min/max constraint, return False
            if not (min_val < node.val < max_val):
                return False

            # Add the left child to the queue with an updated max constraint
            if node.left:
                q.append((node.left, min_val, node.val))

            # Add the right child to the queue with an updated min constraint
            if node.right:
                q.append((node.right, node.val, max_val))

        return True
