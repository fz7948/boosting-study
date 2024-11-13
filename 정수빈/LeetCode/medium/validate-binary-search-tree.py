class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def valid(node, left, right):
            if not node:
                True
            if not (node.vale < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("info"))
        
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().isValidBST(root), True)
root = TreeNode(2, TreeNode(2), TreeNode())

print(Solution().isValidBST(root), False)

