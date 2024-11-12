# 설명: https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
# 두 문자열의 최대 공약수를 구하는 문제입니다. 
# 짧은 문자열을 순회하면서 짧은 문자열의 부분문자열로 긴문자열을 만들 수 있는지 확인합니다. 

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if len(str1) == len(str2) and str1 == str2:
            return str1
        elif len(str1) == len(str2) and str1 != str2:
            return ""
        
        string, long_string = str1, str2

        if len(str1) > len(str2):
            string, long_string = str2, str1
        
        maxLen = 0
        maxStr = ""
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                if len(long_string) % len(string[i:j]) == 0:
                    n = len(long_string) // len(string[i:j])
                    m = len(string) // len(string[i:j])

                    if long_string == string[i:j] * n and string == string[i:j] * m:
                        if maxLen < len(string[i:j]):
                            maxLen = len(string[i:j])
                            maxStr = string[i:j]
        return maxStr