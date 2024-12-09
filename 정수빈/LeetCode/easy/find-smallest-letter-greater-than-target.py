# https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=study-plan-v2&envId=binary-search
# 유형: binary-search
# 시간: 30분

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(list(set(letters)))
        lp, rp = 0, len(letters) -1

        while lp <= rp:
            mp = (lp + rp) // 2
            middle = letters[mp]
            if middle == target:
                break
            elif middle < target:
                lp = mp + 1
            elif middle > target:
                rp = mp - 1

        if 0 < mp + 1 < len(letters):
            if letters[mp] > target:
                return letters[mp]
            else:
                return letters[mp+1]
        else:
            if letters[mp] > target:
                return letters[mp]
            else:
                return letters[0]
            