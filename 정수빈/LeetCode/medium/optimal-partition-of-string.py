# https://leetcode.com/problems/optimal-partition-of-string/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# 난이도: medium 하지만 매우 쉬웠습니다
# 시간: 5분

class Solution:
    def partitionString(self, s: str) -> int:
        ans = []
        tmp = ""
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp += s[i]
            else:
                ans.append(tmp)
                tmp = s[i]
        ans.append(tmp)
        return len(ans)
