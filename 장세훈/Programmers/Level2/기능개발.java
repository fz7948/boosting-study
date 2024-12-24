class 기능개발 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42586
     */

    public int[] solution(int[] progresses, int[] speeds) {
        Deque<Node> queue = new ArrayDeque<>();
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            queue.addLast(new Node(progresses[i], speeds[i]));
        }

        while (!queue.isEmpty()) {
            for (Node node : queue) {
                node.work();
            }

            int count = 0;
            while (!queue.isEmpty() && queue.peekFirst().isDone()) {
                count++;
                queue.pollFirst();
            }

            if (count != 0) answer.add(count);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    class Node {
        int progress;
        int speed;

        public Node(int progress, int speed) {
            this.progress = progress;
            this.speed = speed;
        }

        void work() {
            progress += speed;
        }

        boolean isDone() {
            return progress >= 100;
        }
    }
}
