class 줄서는방법 {
  /*
      https://school.programmers.co.kr/learn/courses/30/lessons/12936
      dfs로 풀면 시간초과
      답을 봤는데, 이런 규칙을 어떻게 찾는지..
   */

  public int[] solution(int n, long k) {
    int[] answer = new int[n];
    List<Integer> list = new ArrayList<>();

    long f = 1;
    for (int i = 1; i <= n; i++) {
      list.add(i);
      f *= i;
    }

    k--;
    int idx = 0;
    while (idx < n) {
      f = f / (n - idx);
      answer[idx++] = list.remove((int) (k / f));
      k = k % f;
    }

    return answer;
  }

}