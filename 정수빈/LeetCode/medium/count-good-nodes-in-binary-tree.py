# https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, visited=[], count = 0):

            if node == None:
                return count
            
            visited.append(node)
            # print(max(visited, key=lambda x: x.val), node.val)
            if node.val == max(visited, key=lambda x: x.val).val:
                count += 1
            count = dfs(node.left, visited, count)
            count = dfs(node.right, visited, count)
            visited.pop()

            return count

        return dfs(node=root, count=0)
