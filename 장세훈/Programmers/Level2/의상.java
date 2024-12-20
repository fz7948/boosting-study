class 의상 {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> map = new HashMap<>();

        for (String[] clothe : clothes) {
            map.put(clothe[1], map.getOrDefault(clothe[1], 1) + 1);
        }


        for (String s : map.keySet()) {
            answer *= map.get(s);
        }

        return answer - 1;
    }
}