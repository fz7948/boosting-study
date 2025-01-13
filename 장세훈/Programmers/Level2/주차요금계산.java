class 주차요금계산 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/92341
     */

    public int[] solution(int[] fees, String[] records) {
        List<Integer> answer = new ArrayList<>();
        Map<String, LocalTime> map = new HashMap<>();
        Map<String, Long> totalTime = new HashMap<>();
        LocalTime lastOut = LocalTime.of(23, 59);

        for (String record : records) {
            String[] split = record.split(" ");
            String[] time = split[0].split(":");
            LocalTime localTime = LocalTime.of(Integer.parseInt(time[0]), Integer.parseInt(time[1]));

            if (split[2].equals("IN")) {
                map.put(split[1], localTime);
            } else {
                LocalTime inTime = map.remove(split[1]);
                totalTime.put(split[1], totalTime.getOrDefault(split[1], 0L) + Duration.between(inTime, localTime).toMinutes());
            }
        }

        for (String key : map.keySet()) {
            LocalTime inTime = map.get(key);
            totalTime.put(key, totalTime.getOrDefault(key, 0L) + Duration.between(inTime, lastOut).toMinutes());
        }

        for (Object carNumber : totalTime.keySet().stream().sorted().toArray()) {
            int addFee = (int) (Math.ceil((double) (totalTime.get(carNumber) - fees[0]) / fees[2]) * fees[3]);
            answer.add(fees[1] + (Math.max(addFee, 0)));
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}