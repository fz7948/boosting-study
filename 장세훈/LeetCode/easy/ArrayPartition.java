package 장세훈.LeetCode.easy;

import java.util.Arrays;

/*
    https://leetcode.com/problems/array-partition/
    561. Array Partition

    정렬한 후 홀수 번쨰의 정수를 더하면 되는 문제
*/

public class ArrayPartition {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
}
