# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# 걸린시간: 10분

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([self.nums[i]*vec.nums[i] for i in range(len(vec.nums))])

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)