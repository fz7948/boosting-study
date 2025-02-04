# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def get_ancestors(p):
            ancestors = []
            while p:
                ancestors.append(p)
                p = p.parent
            return ancestors
        
        p_ans = get_ancestors(p)
        q_ans = get_ancestors(q)
        for p_de in p_ans:
            for q_de in q_ans:
                if p_de == q_de:
                    return p_de