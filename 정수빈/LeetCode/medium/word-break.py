# https://leetcode.com/problems/word-break/submissions/1486078248/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp, 해답 참고
# 난이도: medium
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
