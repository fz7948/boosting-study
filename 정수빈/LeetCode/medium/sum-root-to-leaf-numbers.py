# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
# 시간: 약 20분
# 설명: dfs? 비슷하게 품

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def treeNum(node, sum_num):
            if not node.right and not node.left:
                return sum_num+ str(node.val)
            
            sum_num = sum_num + str(node.val)
            ret = []
            if node.left:
                left = treeNum(node.left, sum_num)
                if isinstance(left, list):
                    ret.extend(left)
                else:
                    ret.append(left)
            if node.right:
                right = treeNum(node.right, sum_num)
                if isinstance(right, list):
                    ret.extend(right)
                else:
                    ret.append(right)
            return ret
        
        ret = treeNum(root, "")
        return sum(map(lambda x: int(x), ret))
