# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/?envType=daily-question&envId=2025-02-21
# 걸린시간 10분

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.root = root

    def find(self, target: int) -> bool:
        q = deque()
        node, val = self.root, self.root.val
        q.append(node)

        while q:
            node = q.popleft()
            val = node.val
            if node.val == target:
                return True

            if node.left:
                node.left.val = 2 * val + 1
                q.append(node.left)
            if node.right:
                node.right.val = 2 * val + 2
                q.append(node.right)
        return False
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)