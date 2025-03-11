# https://leetcode.com/problems/closest-prime-numbers-in-range/
# 중요한 점은 right의 루트 값까지만 소수를 판별하고, 그 이상은 판별하지 않는다.
# 그리고 소수를 판별할 때, 에라토스테네스의 체를 사용한다.

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime_numbers = [True] * (right+1)
        prime_numbers[0] = prime_numbers[1] = False

        for number in range(2, int(right**0.5) + 1):
            if prime_numbers[number] == True:
                for multiple in range(number * number, right + 1, number):
                    prime_numbers[multiple] = False
 
        prime_number_indice = [i for i in range(right+1) if prime_numbers[i]]
        prime_number_indice = [x for x in prime_number_indice if left <= x <= right]
        if len(prime_number_indice) < 2:
            return [-1, -1]
        
        diff = prime_number_indice[1] - prime_number_indice[0] 
        ans = [prime_number_indice[0], prime_number_indice[1]]
        
        for i in range(1, len(prime_number_indice)):
            if diff > prime_number_indice[i] - prime_number_indice[i-1]:
                diff = prime_number_indice[i] - prime_number_indice[i-1]
                ans = [prime_number_indice[i-1], prime_number_indice[i]]
        return ans
