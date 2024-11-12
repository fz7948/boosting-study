# https://leetcode.com/problems/array-of-doubled-pairs/
# 설명: 무작위 숫자의 배열에서 요소가 각 2배가 되게 정렬 할 수 있는가를 물어보는 문제입니다. 
# 해시테이블을 만든 다음에 기존 배열을 절대값으로 정렬한 다음 구했습니다. 
# 다른 풀이를 보면 양수, 음수를 나눠 정렬한 뒤에 구하는 방법도 있더라구요 ㅋㅋ 그게 훨씬 간단헤 보였습니다. 

class Solution(object):
    def canReorderDoubled(self, arr):
        from collections import defaultdict 
        ta = defaultdict(int)
        for a in arr:
            ta[a] += 1
        sorted_arr = sorted(arr, key=lambda x: abs(x))
        for k in sorted_arr:
            if ta[k] > 0 and k * 2 in ta and ta[k*2] > 0:
                ta[k*2] -= 1
                ta[k] -= 1

        for _, v in ta.items():
            if v > 0:
                return False
        return True 
