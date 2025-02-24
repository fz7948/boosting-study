# https://leetcode.com/problems/shortest-word-distance/
# 걸린시간 : 5분

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_index = []
        word2_index = []
        for idx, w in enumerate(wordsDict):
            if w == word1:
                word1_index.append(idx)
            elif w == word2:
                word2_index.append(idx)

        ans = float("inf")
        for w1 in word1_index:
            for w2 in word2_index:
                ans = min(ans, abs(w1-w2))
        return ans