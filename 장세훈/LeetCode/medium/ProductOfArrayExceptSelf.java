package 장세훈.LeetCode.medium;

public class ProductOfArrayExceptSelf {
    /*
     * https://leetcode.com/problems/product-of-array-except-self/description/
     * 238. Product of Array Except Self
        
        배열의 자기 자신을 제외한 나머지의 곱셈 값을 배열로 리턴하는 문제
        모든 수를 곱한 값을 구해 놓고, 배열을 순회하면서 나눗셈을 하면 될 줄 알았으나,
        문제 조건이 나눗셈을 하지 말라고 되어 있음. 그리고 O(N)으로 풀어야 함.

        왼쪽에서 오른쪽 방향으로 곱한 값을 result에 저장
        오른쪽에서 왼쪽으로 곱한 값을 result에 저장
        결과적으로 자기 자신을 제외한 모든 요소의 곱이 됨.
     
     */
    
     public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        int p = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = p;
            p *= nums[i];
        }

        p = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= p;
            p *= nums[i];
        }

        return result;
     }
}
