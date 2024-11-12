# https://leetcode.com/problems/can-place-flowers
# 설명: 0과 1으로 이루어진 배열에서 n개의 1을 인접하지 않게 배치 가능하면 참, 불가능하면 거짓을 반환하는 문제입니다. 
# 배열 맨 앞과 맨끝의 처리를 쉽게 하기 위해 배열 앞뒤로 0을 넣었습니다. 

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            f = flowerbed[i]
            if f == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
            if n <= 0:
                return True
        return False

        