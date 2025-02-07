# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(node, p, path):
            # print(node.val, p.val)
            if node.val == p.val:
                return path + [node]
            if node == None:
                return
            
            path.append(node)
            l,r=None, None
            if node.left:
                l = get_path(node.left, p, path[::])
            if node.right:
                r = get_path(node.right, p, path[::])
            if l:
                return l
            else:
                return r
        
        p_path = get_path(root, p, [])
        q_path = get_path(root, q, [])
        # print(q_path)
        ans = None
        for np in p_path:
            for nq in q_path:
                if np == nq:
                    ans = np
        return ans