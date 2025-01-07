class 영어끝말잇기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12981
     */
    public int[] solution(int n, String[] words) {
        Set<String> set = new HashSet<>();
        int[] arr = new int[n];
        char lastChar = 0;

        for (int i = 0; i < words.length; i++) {
            arr[i % n]++;
            if (set.contains(words[i]) || (i != 0 && lastChar != words[i].charAt(0))) {
                return new int[]{(i % n) + 1, arr[i% n]};
            }

            lastChar = words[i].charAt(words[i].length() - 1);
            set.add(words[i]);
        }

        return new int[]{0, 0};
    }
}