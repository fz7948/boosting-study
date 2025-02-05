# https://leetcode.com/problems/nested-list-weight-sum/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        from collections import deque
        q = []
        nestedList = deque(nestedList)

        def depth(l, count):
            if l.getInteger() == None:
                total = 0
                for n in l.getList():
                    total += depth(n, count+1)
                return total
            else:
                return l.getInteger() * count
                
        ans = []     
        for n in nestedList:
            ans.append(depth(n, 1))
        return sum(ans)