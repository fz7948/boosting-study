# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
# 2글자로 이루어진 문자열 배열을 배치하여 가장 긴 팔린드롬을 만드는 문제 입니다. 
# 해쉬테이블을 이용했고, aa, bb같은 연속된 글자만 따로 처리하였습니다. 
# ab가 있으면 ba가 있어야 팔린드롬이 만들어지니까 ab, ba의 개수의 최소값을 구하였습니다. 

class Solution(object):
    def longestPalindrome(self, words):
        dic = {}
        for w in words:
            if not w in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        answer = 0
        check = False
        for k, v in dic.items():
            if k[0] == k[1]:
                if v > 1:
                    answer += v // 2 * 4
                if v % 2:
                    check = True
                dic[k] = 0
            else:
                rev_k = k[::-1]
                if k in dic and rev_k in dic:
                    answer += min(dic[k], dic[rev_k])  * 4
                    dic[k] = 0
                    dic[rev_k] = 0
        if check:
            answer += 2
        return answer 