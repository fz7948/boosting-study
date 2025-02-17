# https://leetcode.com/problems/letter-tile-possibilities
# 걸린시간 10분 정도

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        ans = set()
        from collections import Counter
        n = len(tiles)

        counter = Counter(tiles)

        def bk(word):
            if len(word) == n:
                ans.add(word)
                return 
            if word:
                ans.add(word)

            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 1
                    bk(word + k)
                    counter[k] += 1
        bk("")
        return len(ans)