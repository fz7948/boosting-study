class 메뉴리뉴얼 {

    /*
            https://school.programmers.co.kr/learn/courses/30/lessons/72411
     */

    Map<String, Integer> map = new HashMap<>();
    Map<Integer, Integer> max = new HashMap<>();

    public String[] solution(String[] orders, int[] course) {
        List<String> list = new ArrayList<>();

        for (String order : orders) {
            char[] charArray = order.toCharArray();
            Arrays.sort(charArray);

            dfs("", charArray, 0);
        }

        for (int c : course) {
            Integer getMax = max.get(c);
            if (getMax > 1) {
                for (String key : map.keySet()) {
                    if (key.length() == c && Objects.equals(map.get(key), getMax)) {
                        list.add(key);
                    }
                }
            }
        }

        String[] array = list.toArray(new String[0]);
        Arrays.sort(array);
        return array;
    }

    void dfs(String str, char[] arr, int start) {
        map.put(str, map.getOrDefault(str, 0) + 1);
        max.put(str.length(), Math.max(map.get(str), max.getOrDefault(str.length(), 0)));

        for (int i = start; i < arr.length; i++) {
            dfs(str + arr[i], arr, i + 1);
        }
    }
}