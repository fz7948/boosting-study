class 방문길이 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/49994
     */
    public int solution(String dirs) {
        Set<String> set = new HashSet<>();
        int[] now = {0, 0};

        for (char c : dirs.toCharArray()) {
            int newX = now[0];
            int newY = now[1];

            if (c == 'U' && newY < 5) {
                newY++;
            } else if (c == 'D' && newY > -5) {
                newY--;
            } else if (c == 'R' && newX < 5) {
                newX++;
            } else if (c == 'L' && newX > -5) {
                newX--;
            } else continue;

            set.add("" + now[0] + now[1] + newX + newY);
            set.add("" + newX + newY + now[0] + now[1]);
            now[0] = newX;
            now[1] = newY;
        }

        return set.size() / 2;
    }
}