class HappyNumber {
    /*
        https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
        202. Happy Number

        주어진 조건에 맞게 숫자를 연산하면서 1이 나오는지 확인
     */
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();

        while (n != 1) {
            int sum = 0;

            while (n != 0) {
                sum += (n % 10) * (n % 10);
                n /= 10;
            }

            if (set.contains(sum)) {
                return false;
            }

            set.add(sum);
            n = sum;
        }

        return true;
    }
}