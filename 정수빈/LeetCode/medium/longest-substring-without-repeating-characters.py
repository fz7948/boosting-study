# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 난이도: medium 
# 시간: 11분 30초
# 설명: 가장 긴 연속된, 반복되지 않은 문자열을 반환하는 문제입니다. 
# 왼쪽 포인터를 선언하여 순회하면서 반복되는 게 있으면 포인터를 다시 앞으로 옮기고 다시 순회했습니다. 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lp = 0
        dup = []
        max_ans = 0

        while lp < len(s):
            if not s[lp] in dup:
                dup.append(s[lp])
            else:
                max_ans = max(len("".join(dup)), max_ans)
                lp = lp - len(dup) + 1
                dup = [s[lp]]
                
            lp += 1
        max_ans = max(len("".join(dup)), max_ans)

        return max_ans