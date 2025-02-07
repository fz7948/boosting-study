# https://leetcode.com/problems/tuple-with-same-produc
# 걸린시간: 40분 
# 계속 brute force로 풀었다가 타임아웃이 났다. 답을 보고 4sum, 3sum과 같은 방식이라는 걸 알았다. ㅠㅠ  

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pair_products_frequency = {}
        total_number_of_tuple = 0

        for i in range(n):
            for j in range(i+1, n):
                product_value = nums[i] * nums[j]
                if not product_value in pair_products_frequency:
                    pair_products_frequency[product_value] = 0
                pair_products_frequency[product_value] += 1

        for product_frequency in pair_products_frequency.values():
            pairs_of_equal_product = (product_frequency-1) * product_frequency // 2

            total_number_of_tuple += 8*pairs_of_equal_product
        return total_number_of_tuple
                    