# https://leetcode.com/problems/valid-word-abbreviation/description/
# 난이도: easy
# 시간: 30분 이상
# 이상하게 easy문제인데도 오래걸렸네요 ㅠ

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        from collections import deque

        qword = deque(list(abbr))
        word2 = []
        while qword:
            c = qword.popleft()
            nums = []
            while str.isdigit(c):
                nums.append(c)
                
                if not qword:
                    break
                c = qword.popleft()
                
            if nums:
                word2.append("".join(nums))
            if not str.isdigit(c):
                word2.append(c)

        # print(word2)
        idx = 0
        for i in range(len(word2)):
            if not str.isdigit(word2[i]):
                if idx < len(word) and word2[i] == word[idx]:
                    idx +=1
                else:
                    return False
            else:
                if len(word2[i]) > 0 and word2[i][0] == "0":
                    return False
                if idx + int(word2[i]) > len(word):
                    return False
                idx += int(word2[i])

                    
        # print(idx, len(word))
        return idx == len(word)

                
            


