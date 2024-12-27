class HIndex {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=java
    */
    public int solution(int[] citations) {
        Arrays.sort(citations);

        for (int i = 0; i < citations.length / 2; i++) {
            int temp = citations[i];
            citations[i] = citations[citations.length - 1 - i];
            citations[citations.length - 1 - i] = temp;
        }

        for (int i = citations[0]; i > 0; i--) {
            int count = 0;
            for (int j = 0; j < citations.length; j++) {
                if (i <= citations[j])
                    count++;
                else break;
            }

            if (count >= i && citations.length - count <= i) {
                return i;
            }
        }

        return 0;
    }
}