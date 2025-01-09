class 튜플 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/64065
     */

    public int[] solution(String s) {
        List<List<Integer>> lists = new ArrayList<>();
        String[] split = s.replace("},", " ").replace("{", "").replace("}", "").split(" ");

        for (String string : split) {
            List<Integer> list = new ArrayList<>();
            for (String n : string.split(",")) {
                list.add(Integer.parseInt(n));
            }
            lists.add(list);
        }

        lists.sort(Comparator.comparingInt(List::size));

        List<Integer> answer = new ArrayList<>();
        Set<Integer> set = new HashSet<>();

        for (List<Integer> list : lists) {
            for (Integer i : list) {
                if (!set.contains(i)) {
                    set.add(i);
                    answer.add(i);
                }
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}