
# https://leetcode.com/problems/summary-ranges
# 난이도 : easy
# 시간: 22분
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums:
            return []
        s = [nums[0]]
        for i in range(1, len(nums)):
            n = nums[i]
            if s and n - s[-1] == 1:
                s.append(n)
            else:
                ans.append(s)
                s = [n]
        
        if s:
            ans.append(s)

        answer = []
        for a in ans:
            if len(a) > 1:
                s = f"{a[0]}->{a[-1]}"
                answer.append(s)
            elif len(a) == 1:
                s = f"{a[0]}"
                answer.append(s)
        return answer