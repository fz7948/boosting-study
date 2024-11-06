/*
    다음 큰 숫자
    https://school.programmers.co.kr/learn/courses/30/lessons/12911

    n의 2진수의 1의 개수 구하기 => 2로 나머지 연산해서 1이 나오면 카운팅
    Integer.bitCount(n) 메서드를 사용해서 1의 개수를 간단하게 구할 수도 있음.

*/

class Solution {
    public int solution(int n) {
        int nOneCount = countOne(n);
        for (int i = n + 1; ; i++) {
            if (nOneCount == countOne(i))
                return i;
        }
    }
    
public int countOne(int n) {
    int count = 0;

    while (n > 0) {
        if (n % 2 == 1)
            count++;
        n /= 2;
    }
    
    return count;
}