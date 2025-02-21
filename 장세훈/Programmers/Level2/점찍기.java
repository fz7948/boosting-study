class 점찍기 {

  /*
     https://school.programmers.co.kr/learn/courses/30/lessons/140107
    
   */

  public long solution(int k, int d) {
    long count = 0;

    for (int x = 0; x <= d; x += k) {
      long yMax = (long) Math.sqrt((long) d * d - (long) x * x);
      count += (yMax / k) + 1;
    }

    return count;
  }
}
