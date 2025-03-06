# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import Counter
        distinct_character = set()
        ans = 0
        lp, rp = 0, 0
        while lp < len(s):
            if len(distinct_character) < 2 and rp < len(s):
                distinct_character.add(s[rp])
                rp += 1
                ans = max(ans, rp-lp)
            elif len(distinct_character) == 2 and rp < len(s) and s[rp] in distinct_character:
                rp += 1
                ans = max(ans, rp-lp)
            else:
                lp += 1
                rp = min(lp + ans, len(s))
                
                counter = Counter(s[lp: rp])
                distinct_character = set(counter.keys())

        return ans