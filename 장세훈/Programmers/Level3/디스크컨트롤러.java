class 디스크컨트롤러 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=java

     */

    public int solution(int[][] jobs) {
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        int currentTime = 0;
        int totalTime = 0;
        int jobIndex = 0;
        int doneCount = 0;

        while (doneCount < jobs.length) {
            while (jobIndex < jobs.length && jobs[jobIndex][0] <= currentTime) {
                pq.offer(jobs[jobIndex]);
                jobIndex++;
            }

            if (pq.isEmpty()) {
                currentTime = jobs[jobIndex][0];
            } else {
                int[] job = pq.poll();
                currentTime += job[1];
                totalTime += currentTime - job[0];
                doneCount++;
            }
        }

        return totalTime / jobs.length;
    }
}