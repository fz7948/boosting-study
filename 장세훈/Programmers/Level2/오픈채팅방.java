class 오픈채팅방 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42888
     */
    public String[] solution(String[] record) {
        Map<String, String> ids = new HashMap<>();
        List<String[]> list = new ArrayList<>();

        for (String op : record) {
            String[] split = op.split(" ");

            if (split[0].equals("Enter")) {
                ids.put(split[1], split[2]);
                list.add(new String[]{split[1], "님이 들어왔습니다."});
            } else if (split[0].equals("Leave")) {
                list.add(new String[]{split[1], "님이 나갔습니다."});
            } else {
                ids.put(split[1], split[2]);
            }
        }

        return list.stream().map(s -> ids.get(s[0]) + s[1]).toArray(String[]::new);
    }
}