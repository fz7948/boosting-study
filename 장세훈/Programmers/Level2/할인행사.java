class 할인행사 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/131127
     */

    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }

        int lt = 0;

        for (int rt = 0; rt < discount.length; rt++) {
            if (map.containsKey(discount[rt])) {
                map.put(discount[rt], map.get(discount[rt]) - 1);
            }

            if (rt - lt + 1 == 10) {
                boolean isOk = true;
                for (String key : map.keySet()) {
                    if (map.get(key) > 0) {
                        isOk = false;
                        break;
                    }
                }

                if (isOk) {
                    answer++;
                }

                if (map.containsKey(discount[lt])) {
                    map.put(discount[lt], map.get(discount[lt]) + 1);
                }
                lt++;
            }
        }
        return answer;
    }
}