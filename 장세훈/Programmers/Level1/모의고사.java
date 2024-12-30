class 모의고사 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=java
     */
    public int[] solution(int[] answers) {
        int[][] supos = new int[][]{
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        int[] score = new int[3];
        int maxScore = 0;

        for (int i = 0; i < supos.length; i++) {
            int index = 0;
            for (int answer : answers) {
                if (answer == supos[i][index])
                    score[i]++;

                index = (index + 1) % supos[i].length;
            }

            maxScore = Math.max(maxScore, score[i]);
        }

        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (score[i] == maxScore)
                answer.add(i + 1);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
