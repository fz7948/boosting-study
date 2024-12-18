class 폰켓몬 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=java
        간단 해시 문제
    */

    public int solution(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        return Math.min(set.size(), nums.length);
    }
}