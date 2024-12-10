class 이중우선순위큐 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42628

        이중우선순위 큐 만들기
        오름차순 우선순위 큐, 내림차순 우선순위 큐를 활용
    */
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        PriorityQueue<Integer> rpq = new PriorityQueue<>(Collections.reverseOrder());

        for (String operation : operations) {
            String[] s = operation.split(" ");
            if (s[0].equals("I")) {
                Integer i = Integer.valueOf(s[1]);
                pq.add(i);
                rpq.add(i);
            } else if (s[1].equals("1") ) {
                pq.remove(rpq.poll());
            } else if (s[1].equals("-1")) {
                rpq.remove(pq.poll());
            }
        }

        if(pq.isEmpty())
            return new int[]{0, 0};
        else
            return new int[]{rpq.peek(), pq.peek()};
    }
}