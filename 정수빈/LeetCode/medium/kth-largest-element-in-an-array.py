# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapnum = []
        for n in nums:
            heapq.heappush(heapnum, -n)
        answer = None
        for _ in range(k):
            answer = heapq.heappop(heapnum)
        return -answer