// https://leetcode.com/problems/two-sum/

function twoSum(nums: number[], target: number): number[] {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    if (map[nums[i]] >= 0) {
      return [map[nums[i]], i];
    }
    map[target-nums[i]] = i;
  }
};
