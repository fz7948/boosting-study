# https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75
# 설명: 다음 큰 수의 인덱스를 구하는 문제
# 스택을 사용해서 해결

class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = [] #(temp, idx)
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append([t, idx])
        return res
        