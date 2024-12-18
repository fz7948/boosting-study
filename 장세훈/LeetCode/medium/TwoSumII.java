class TwoSumII {
    /*
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1476143516/
        투포인터
     */

    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;

        while (left != right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target)
                return new int[]{left + 1, right + 1};
            else if (sum < target) {
                left++;
            } else right--;
        }

        return null;
    }
}