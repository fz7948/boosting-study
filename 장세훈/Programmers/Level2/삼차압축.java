class 삼차압축 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/17684
     */
    public int[] solution(String msg) {
        List<Integer> list = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        int index = 1;
        for (int i = 'A'; i <= 'Z'; i++) {
            map.put((char) i + "", index++);
        }

        while (!msg.isEmpty()) {
            for (int j = 1; j <= msg.length(); j++) {
                String substring = msg.substring(0, j);
                if (!map.containsKey(substring)) {
                    map.put(substring, index++);
                    list.add(map.get(msg.substring(0, j - 1)));
                    msg = msg.substring(j - 1);
                    break;
                }
            }
            if (map.containsKey(msg)) {
                list.add(map.get(msg));
                break;
            }
        }

        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}