# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# 설명: 1차원 배열에서 2개의 요소의 합이 60으로 나눠지는 조합을 찾는 문제입니다. 
# 해시테이블을 이용해서 나머지를 테이블에 저장하였습니다. 

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        answer = 0
        dct = {}

        for _, t in enumerate(time):
            dct[t%60] = dct.get(t%60, 0) + 1
        for k, v in dct.items():
            if  k == 0 or k == 30:
                answer += v * (v - 1) // 2
                dct[k] = 0
            elif 60 - k in dct:
                answer += (v * dct.get(60 - k, 1))
                dct[k] = 0
                dct[60-k] = 0

        return int(answer)
                

print(numPairsDivisibleBy60([30,20,150,100,40]), 3)
print(numPairsDivisibleBy60([60,60,60]), 3)
print(numPairsDivisibleBy60([20,40]), 1)