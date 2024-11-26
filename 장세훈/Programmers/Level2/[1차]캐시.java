class Cache {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/17680
        [1차] 캐시

        cache hit  -> 1
        cache miss -> 5

        queue를 사용해서 LRU 구현

     */
    public int solution(int cacheSize, String[] cities) {
        Deque<String> queue = new ArrayDeque<>();
        int answer = 0;

        for (String city : cities) {
            String lowerCase = city.toLowerCase();

            if (queue.contains(lowerCase)) {
                answer += 1;
                queue.remove(lowerCase);
            } else
                answer += 5;

            queue.addFirst(lowerCase);

            if (queue.size() > cacheSize) queue.pollLast();
        }

        return answer;
    }
}