# https://leetcode.com/problems/minimum-number-of-keypresses/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# 아마존 기출 문제 

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = sorted(Counter(s).items(), key=lambda x: -x[1])
        once_press_set = set()
        twice_press_set = set()
        third_press_set = set()
        for i, (k, v) in enumerate(counter):
            if i < 9:
                once_press_set.add(k)
            elif i >= 9 and i < 18:
                twice_press_set.add(k)
            else:
                third_press_set.add(k)
        ans = 0
        for c in s:
            if c in once_press_set:
                ans += 1
            elif c in twice_press_set:
                ans += 2
            else:
                ans += 3

        return ans