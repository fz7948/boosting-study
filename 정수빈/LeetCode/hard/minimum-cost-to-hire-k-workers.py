# https://leetcode.com/problems/toeplitz-matrix/
# 시간초과 ㅠㅠ

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        import heapq
        total = float("inf")
        for i in range(len(quality)):
            mod = quality[i]
            satisfy = []
            heapq.heapify(satisfy)
            for j in range(len(quality)):
                if wage[j] <= quality[j] / mod * wage[i]:
                    heapq.heappush(satisfy, quality[j] / mod * wage[i])
            
            if len(satisfy) >= k:
                s = 0
                for t in range(k):
                    s += heapq.heappop(satisfy)
                

                total = min(total, s)
        return total