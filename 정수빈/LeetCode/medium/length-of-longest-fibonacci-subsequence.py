# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# 난이도: medium
# 걸린시간: 20분

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        from collections import Counter
        counter = Counter(arr)
        self.ans = 0
        def fibo_like(prev, curr, count):
            self.ans = max(self.ans, count)
            fibo = prev + curr
            if fibo in counter:
                fibo_like(curr, fibo, count+1)
            else:
                return
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] in counter:
                    fibo_like(arr[j], arr[i] + arr[j], 3)
        return self.ans
        