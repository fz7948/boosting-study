class 소수찾기 {

    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=java
        
        완전 탐색
        모든 숫자를 조합해 만들고 소수 카운팅
     */

    Set<Integer> set = new HashSet<>();
    boolean[] sosu = new boolean[10000000];

    public int solution(String numbers) {
        initSosu();
        dfs("0", numbers, new boolean[10000000]);
        return set.size();
    }

    void initSosu() {
        Arrays.fill(sosu, true);
        sosu[0] = false;
        sosu[1] = false;

        for (int i = 2; i < sosu.length; i++) {
            if (sosu[i]) {
                for (int j = i + i; j < sosu.length; j += i)
                    sosu[j] = false;
            }
        }
    }

    void dfs(String num, String numbers, boolean[] visit) {
        if (sosu[Integer.parseInt(num)]) set.add(Integer.parseInt(num));
        if (num.length() == numbers.length() + 1) return;

        for (int i = 0; i < numbers.length(); i++) {
            if (!visit[i]) {
                visit[i] = true;
                dfs(num + numbers.charAt(i), numbers, visit);
                visit[i] = false;
            }
        }
    }
}