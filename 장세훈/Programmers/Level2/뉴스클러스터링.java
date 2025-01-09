class 뉴스클러스터링 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/17677
     */

    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        Map<String, Integer> map1 = new HashMap<>();
        Map<String, Integer> map2 = new HashMap<>();

        for (int i = 0; i < str1.length() - 1; i++) {
            if (Character.isAlphabetic(str1.charAt(i)) && Character.isAlphabetic(str1.charAt(i + 1))) {
                String string = str1.subSequence(i, i + 2).toString();
                map1.put(string, map1.getOrDefault(string, 0) + 1);
            }
        }

        for (int i = 0; i < str2.length() - 1; i++) {
            if (Character.isAlphabetic(str2.charAt(i)) && Character.isAlphabetic(str2.charAt(i + 1))) {
                String string = str2.subSequence(i, i + 2).toString();
                map2.put(string, map2.getOrDefault(string, 0) + 1);
            }
        }

        int sum = 0;
        int union = 0;

        for (String key : map1.keySet()) {
            if (map2.containsKey(key)) {
                sum += Math.max(map1.get(key), map2.get(key));
                union += Math.min(map1.get(key), map2.get(key));
            } else
                sum += map1.get(key);
        }

        for (String key : map2.keySet()) {
            if (!map1.containsKey(key)) {
                sum += map2.get(key);
            }
        }

        if (map1.isEmpty() && map2.isEmpty()) return 65536;

        return (int) (65536 * ((double) union / (sum)));
    }
}