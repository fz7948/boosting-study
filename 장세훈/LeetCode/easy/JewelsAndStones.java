lass JewelsAndStones {
    /*
        771.Jewels and Stones
        https://leetcode.com/problems/jewels-and-stones/description/

        jewels 문자를 set에 담는다.
        stones 순회하며 문자가 set에 있다면 answer++

     */

    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> set = new HashSet<>();
        int answer = 0;

        for (char c : jewels.toCharArray()) {
            set.add(c);
        }

        for (char c : stones.toCharArray()) {
            if(set.contains(c))
                answer++;
        }

        return answer;
    }
}