# https://leetcode.com/problems/reorganize-string/description/?envType=problem-list-v2&envId=greedy
# 이것도 답지 참고해서 ㅠㅠ
# 난이도: medium
# 시간: 32분
# 유형: greedy, 더 괜찮게 하면 heapqueue도 된다하네요 

from collections import Counter

class Solution:
            
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = list(map(list, sorted(Counter(s).items(), key=lambda x: -x[1])))
        i = 0
        prev = None
        ans = ""
        while i < n:
            counter = sorted(counter, key=lambda x: -x[1])
            cur_idx = 0
            if prev != None and prev[0] == counter[cur_idx][0]:
                cur_idx += 1
            # print(cur_idx)
            if cur_idx > len(counter)-1:
                return ""
            if counter[cur_idx][1] > 0:
                ans += counter[cur_idx][0]
                counter[cur_idx][1] -= 1
            prev = counter[cur_idx]
            i +=1
        if len(s) == len(ans):
            return ans
        return ""

