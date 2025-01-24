class 최고의집합 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12938
        흠. 풀이는 맞았는데 효율성에서 떨어짐.
        answer 타입을 List에서 배열로 바꾸니 정답.
        List는 Integer를 생성해서 저장하다보니 리소스를 많이 먹나 봄.
     */

    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        int index = 0;

        while (s != 0) {
            if (s / n == 0) return new int[]{-1};
            answer[index++] = s / n;
            s = s - s / n;
            n--;
        }

        return answer;
    }
}