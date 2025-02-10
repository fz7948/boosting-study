# https://leetcode.com/problems/binary-tree-upside-down/?envType=problem-list-v2&envId=depth-first-search
# 걸린시간: 40분 답지봄 ㅠㅠㅠ 아 이렇게 쉬운데 왜 못푸는지 슬프네요 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recursive(node, parent=None, right=None):
            if not node:
                return parent
            res = recursive(node.left, node, node.right)
            node.right = parent
            node.left = right
            return res
        return recursive(root)
