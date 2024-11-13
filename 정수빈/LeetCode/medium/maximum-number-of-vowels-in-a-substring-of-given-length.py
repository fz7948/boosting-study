# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# 설명: 슬라이딩 윈도우 k개의 연속된 모음의 개수를 세는 문제입니다. 첫번째 k 길이의 문자열에서 연속된 모음의 개수를 셉니다. 
# 순회하면서 다음칸에 모음이 있다면 +1 포함됐던 모음이 빠진다면 -1

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = "aeiou"
        maxStr = s[:k]
        count = 0

        for ss in maxStr:
            if ss in vowel:
                count += 1
            if count == k:
                return k
        maxCount = count
        for i in range(k, len(s)):
            if s[i-k] in vowel:
                count -=1
            if s[i] in vowel:
                count +=1
            maxCount = max(maxCount, count)
            if k == maxCount:
                return k
        return maxCount