# https://leetcode.com/problems/factorial-trailing-zeroes
# 설명: 팩토리얼수에 끝에 0의 개수를 세는 것, 생각보다 개선할점이 많아서 신기
# 지금은 O(n)이지만, O(logN)으로 푸는 방법도 존재 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_five = 0
        for i in range(5, n+1, 5):
            n = i
            if n % 5 == 0:
                while n % 5 == 0:
                    count_five +=1
                    n //= 5

        return count_five