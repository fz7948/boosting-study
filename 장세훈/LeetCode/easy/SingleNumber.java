class Solution {
    /*
        https://leetcode.com/problems/single-number/description/
        요소가 하나인 숫자를 찾는 문제. 나머진 쌍을 이룸
        비트 연산 xor을 활용
        xor을 두변 연산하면 원래의 수로 돌아온다는 특징이있음
    */
    public int singleNumber(int[] nums) {
        int result = 0;
        for(int num : nums) {
            result ^= num;
        }

        return result;
    }
}