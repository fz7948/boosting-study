# https://leetcode.com/problems/3sum-with-multiplicity
# 설명: 3개의 숫자 합이 target이 되는 방법의 갯수를 구하는 문제입니다. 
# 숫자 2개를 합한 값을 해시테이블에 넣어주고 개수를 구합니다. (3개의 숫자가 모두 다른 경우)
# 숫자가 2개가 동일한 값, 숫자가 3개가 동일한 값인 경우를 따로 구합니다. 

from collections import Counter

class Solution(object):
    def threeSumMulti(self, arr, target):

        answer = 0
        dic = Counter(arr)
        dup = {}
        for k1 in dic.keys():
            for k2 in dic.keys():
                t = target - k1 - k2
                if t in dic and not(t == k1) and not(t == k2) and not (k1 == k2):
                    pair = tuple(sorted([k1, k2, t]))
                    if pair in dup:
                        pass
                    else:
                        answer += dic[k1] * dic[k2] * dic[t]
                        dup[pair] = 1

        for k1 in dic.keys():
            t = target - k1*2
            if t in dic and not (t == k1):
                answer += dic[k1] * (dic[k1]-1) * dic[t] // 2

        for k1 in dic.keys():
            t = target - k1*2
            if t == k1 and dic[k1] >= 3:
                answer +=  dic[k1] * ( dic[k1]-1) * ( dic[k1]-2) // 6

        return answer % (10 ** 9 + 7)