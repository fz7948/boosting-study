class 구명보트 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42885
     */
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int lt = 0, rt = people.length - 1;

        while (lt <= rt) {
            if (people[lt] + people[rt] <= limit) lt++;
            rt--;
            answer++;
        }

        return answer;
    }
}