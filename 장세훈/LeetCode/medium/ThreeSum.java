class ThreeSum {
    /*
        15. 3Sum
        https://leetcode.com/problems/3sum/description/

        세개의 숫자를 더해서 0이 되는 경우를 찾아서 반환하는 문제
        중복되는 경우는 제외하고 반환

        3중 for문으로 풀 경우 timeout 발생


        O(n^2)으로 풀이
         - 하나의 숫자를 고정한 상태에서 투포인트(left, right)으로 나머지 두 숫자를 찾는 방식으로 풀이
         - left > right 일 경우 다음 숫자가 고정되면서 left, right 초기화 -> 반복
            
     */

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int left = i + 1;
            int right = nums.length - 1;

            // 중복된 값 건너뛰기
            if(i > 0 && nums[i] == nums[i-1]) continue;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    answer.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // 중복된 값 건너뛰기
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                }
            }
        }

        return answer;
    }
}