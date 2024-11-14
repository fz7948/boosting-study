class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def same(p, q):

            if p == None and q == None:
                return True
            elif p == None and q:
                return False
            elif p and q == None:
                return False
            
            if p.val != q.val:
                return False
            
            return (same(p.left, q.left) and same(p.right, q.right))
        
        return same(p,q)