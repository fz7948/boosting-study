# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Node({self.val})"
    
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def dfs(node, visited_order=[]):
            if node == None:
                prev = None
                length = 0
                arr_length = []
                for v in visited_order:
                    if prev != v:
                        length += 1
                    else:
                        arr_length.append(length)
                        length = 1
                    prev = v
                if arr_length:
                    return max(arr_length)
                else:
                    return 0
            

            a = dfs(node.left, visited_order + [False]) # left is False
            b = dfs(node.right, visited_order + [True]) # right is True

            return max(a,b)
        return dfs(root)
    
# 아래는 정답 위는 메모리 아웃이 남
# class Solution(object):
#     def longestZigZag(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         self.maxi = 0

#         def dfs(node, left, right):
#             self.maxi = max(self.maxi, left, right)

#             if node.left:
#                 dfs(node.left, right + 1, 0)

#             if node.right:
#                 dfs(node.right, 0, left + 1)

#         dfs(root, 0, 0)
#         return self.maxi
    
