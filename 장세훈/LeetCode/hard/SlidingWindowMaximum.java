class SlidingWindowMaximum {
    /*
        https://leetcode.com/problems/sliding-window-maximum/description/
        슬라이딩 윈도우 k 크기의 범위 안에 있는 가장 큰 수들을 반환
        부르트 포스로 풀면 시간 초과
        데크로 윈도우의 가장 큰수 인덱스를 저장
     */

    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> result = new ArrayList<>();
        Deque<Integer> dq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            if (!dq.isEmpty() && dq.peek() < i - k + 1)
                dq.poll();
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i])
                dq.pollLast();
            dq.add(i);

            if (i >= k - 1)
                result.add(nums[dq.peek()]);

        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
