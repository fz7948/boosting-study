class 다리를지나는트럭 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=java
        
     */
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Deque<Integer> queue = new ArrayDeque<>();
        Deque<int[]> list = new ArrayDeque<>();

        for (int truckWeight : truck_weights) {
            queue.addLast(truckWeight);
        }

        int w = 0;
        while (!queue.isEmpty() || !list.isEmpty()) {
            for (int[] ints : list) {
                if (++ints[1] >= bridge_length) {
                    w -= ints[0];
                    list.pollFirst();
                }
            }

            if (!queue.isEmpty() && weight >= w + queue.peekFirst() && bridge_length >= list.size()+1) {
                Integer poll = queue.pollFirst();
                w += poll;
                list.addLast(new int[]{poll, 0});
            }

            answer++;
        }

        return answer;
    }
}