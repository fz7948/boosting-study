class 멀쩡한사각형 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/62048
     */

    public long solution(int w, int h) {
        long answer = (long) w * (long) h;

        while (w != h) {
            int max = Math.max(w, h);
            int min = Math.min(w, h);
            answer -= min;
            w = max - min;
            h = min;
        }

        return answer - w;
    }

}